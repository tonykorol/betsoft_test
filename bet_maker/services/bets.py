import httpx
from fastapi import HTTPException
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from bet_maker.config import settings
from bet_maker.models.bets import Bet
from bet_maker.schemas.bets import BetCreateRequest, BetUpdateStatusRequest


async def get_all_bets_service(session: AsyncSession) -> list[Bet]:
    query = select(Bet)
    result: Result = await session.execute(query)
    return result.scalars().all()


async def check_event_exist(event_id) -> bool:
    url = f"{settings.LINE_PROVIDER_URL}/events/{event_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return True


async def create_bet_service(bet_data: BetCreateRequest, session: AsyncSession) -> Bet:
    if not await check_event_exist(bet_data.event_id):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Invalid event id")
    new_bet: Bet = Bet(**bet_data.model_dump())
    session.add(new_bet)
    await session.commit()
    await session.refresh(new_bet)
    return new_bet


async def get_bet_by_id(bet_id: int, session: AsyncSession) -> Bet:
    query = select(Bet).filter(Bet.id == bet_id)
    result: Result = await session.execute(query)
    bet: Bet = result.scalar_one_or_none()
    if not bet:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Invalid bet id")
    return bet


async def get_all_bets_by_event_id(event_id: int, session: AsyncSession) -> list[Bet]:
    query = select(Bet).filter(Bet.event_id == event_id)
    result: Result = await session.execute(query)
    return result.scalars().all()


async def update_bets_status_service(payload: BetUpdateStatusRequest, session: AsyncSession) -> Bet:
    bets: list[Bet] = await get_all_bets_by_event_id(payload.event_id, session)
    if not bets:
        HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No bets found for this event")
    for bet in bets:
        bet.status = payload.status
    await session.commit()

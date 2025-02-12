import httpx
from fastapi import HTTPException
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from bet_maker.config import settings
from bet_maker.models.bets import Bet
from bet_maker.schemas.bets import BetCreateRequest, BetUpdateStatusRequest


async def get_all_bets_service(session: AsyncSession) -> list[Bet]:
    """
    Service function for get all bets
    :param session:
    :return:
    """
    query = select(Bet)
    result: Result = await session.execute(query)
    return result.scalars().all()


async def check_event_exist_and_not_ended(event_id) -> bool:
    """
    Check event exist and not ended
    :param event_id:
    :return:
    """
    url = f"{settings.LINE_PROVIDER_URL}/events/{event_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200 and response.json()["state"] == 1:
            return True


async def create_bet_service(bet_data: BetCreateRequest, session: AsyncSession) -> Bet:
    """
    Service function for create new bet
    :param bet_data:
    :param session:
    :return:
    """
    if not await check_event_exist_and_not_ended(bet_data.event_id):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Invalid event id or event has ended")

    new_bet: Bet = Bet(**bet_data.model_dump())
    session.add(new_bet)
    await session.commit()
    await session.refresh(new_bet)
    return new_bet


async def get_bet_by_id(bet_id: int, session: AsyncSession) -> Bet:
    """
    Service function for get one bet by id
    :param bet_id:
    :param session:
    :return:
    """
    query = select(Bet).filter(Bet.id == bet_id)
    result: Result = await session.execute(query)
    bet: Bet = result.scalar_one_or_none()
    if not bet:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Invalid bet id")
    return bet


async def get_all_bets_by_event_id(event_id: int, session: AsyncSession) -> list[Bet]:
    """
    Service function for get all bets by event id
    :param event_id:
    :param session:
    :return:
    """
    query = select(Bet).filter(Bet.event_id == event_id)
    result: Result = await session.execute(query)
    return result.scalars().all()


async def update_bets_status_service(payload: BetUpdateStatusRequest, session: AsyncSession) -> Bet:
    """
    Service function for update bets status
    :param payload:
    :param session:
    :return:
    """
    bets: list[Bet] = await get_all_bets_by_event_id(payload.event_id, session)
    if not bets:
        HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No bets found for this event")
    for bet in bets:
        bet.status = payload.status
    await session.commit()

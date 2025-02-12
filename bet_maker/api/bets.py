from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from bet_maker.database.db import get_async_session
from bet_maker.models.bets import Bet
from bet_maker.schemas.bets import BetCreateRequest, BetUpdateStatusRequest, GetAllBetsResponse, OneBetResponse
from bet_maker.services.bets import create_bet_service, get_all_bets_service, get_bet_by_id, update_bets_status_service

router = APIRouter(prefix="/bets", tags=["Bets"])


@router.get(
    path="",
    response_model=GetAllBetsResponse,
)
async def get_all_bets(
        session: AsyncSession = Depends(get_async_session),
):
    """
    Handler for get all bets
    :param session:
    :return:
    """
    bets: list[Bet] = await get_all_bets_service(session)
    return GetAllBetsResponse(bets=[b.to_pydantic_schema() for b in bets])


@router.post(
    path="",
    response_model=OneBetResponse,
)
async def create_bet(
        bet_data: BetCreateRequest,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Handler for create bet
    :param bet_data:
    :param session:
    :return:
    """
    new_bet: Bet = await create_bet_service(bet_data, session)
    return OneBetResponse(bet=new_bet.to_pydantic_schema())


@router.get(
    path="/{bet_id}",
    response_model=OneBetResponse,
)
async def get_one_bet(
        bet_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Handler for get one bet by id
    :param bet_id:
    :param session:
    :return:
    """
    bet: Bet = await get_bet_by_id(bet_id, session)
    return OneBetResponse(bet=bet.to_pydantic_schema())


@router.post(
    path="/webhook",
)
async def webhook(
        payload: BetUpdateStatusRequest,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Handler for update bets status
    :param payload:
    :param session:
    :return:
    """
    await update_bets_status_service(payload, session)
    return {"message": "ok"}

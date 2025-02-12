from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from bet_maker.models.bets import BetStatus


class BetBaseSchema(BaseModel):
    event_id: int
    amount: Decimal


class BetSchema(BetBaseSchema):
    id: int
    status: BetStatus
    created_at: datetime


class OneBetResponse(BaseModel):
    bet: BetSchema


class GetAllBetsResponse(BaseModel):
    bets: list[BetSchema]


class BetCreateRequest(BetBaseSchema):
    pass


class BetUpdateStatusRequest(BaseModel):
    event_id: int
    status: BetStatus

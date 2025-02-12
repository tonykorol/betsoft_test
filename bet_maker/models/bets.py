from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any

from sqlalchemy import DECIMAL, TIMESTAMP, Integer
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from bet_maker.models.base import Base


class BetStatus(Enum):
    PENDING = 1
    WON = 2
    LOST = 3


class Bet(Base):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer)
    amount: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    status: Mapped[BetStatus] = mapped_column(SQLEnum(BetStatus), default=BetStatus.PENDING)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now(), nullable=False)

    def to_pydantic_schema(self) -> Any:
        from bet_maker.schemas.bets import BetSchema

        return BetSchema(**self.__dict__)

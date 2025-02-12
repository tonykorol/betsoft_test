import decimal
import enum

from pydantic import BaseModel


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(BaseModel):
    event_id: int
    coefficient: decimal.Decimal | None = None
    deadline: int | None = None
    state: EventState | None = None


class GetAvailableEventsResponse(BaseModel):
    events: list[Event]

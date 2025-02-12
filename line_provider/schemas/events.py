import decimal
import enum
from typing import Optional

from pydantic import BaseModel


class EventState(enum.Enum):
    NEW = 1
    FINISHED_WIN = 2
    FINISHED_LOSE = 3


class Event(BaseModel):
    event_id: int
    coefficient: Optional[decimal.Decimal] = None
    deadline: Optional[int] = None
    state: Optional[EventState] = None


class EventCreateRequest(Event):
    pass


class EventCreateResponse(BaseModel):
    payload: Event


class EventsGetResponse(BaseModel):
    events: list[Event]


class EventGetResponse(BaseModel):
    payload: Event


class EventUpdateRequest(BaseModel):
    state: EventState

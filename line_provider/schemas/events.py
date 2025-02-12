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

import time

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from ..schemas.events import EventCreateRequest, Event, EventState, EventUpdateRequest
from ..utils.events_data import events


async def check_event_exist(event_id: int) -> bool:
    return str(event_id) in events.keys()

async def create_new_event(event: EventCreateRequest) -> Event:
    if await check_event_exist(event.event_id):
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"Event with id {event.event_id} already exist")
    events[str(event.event_id)] = event
    return event

async def get_events() -> list[Event]:
    all_events = list(e for e in events.values() if time.time() < e.deadline)
    return all_events

async def get_event_by_id(event_id: int) -> Event:
    try:
        event: Event = events[str(event_id)]
    except KeyError:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Invalid event id")
    return event

async def update_event_status(event_id: int, status: EventUpdateRequest) -> Event:
    event: Event = await get_event_by_id(event_id)
    event.state = status.state
    return event

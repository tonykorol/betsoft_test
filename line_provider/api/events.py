from fastapi import APIRouter

from ..schemas.events import EventCreateRequest, Event, EventsGetResponse, EventUpdateRequest
from ..services.events import create_new_event, get_events, get_event_by_id, update_event_status

router = APIRouter(prefix='/events', tags=["Events"])

@router.post(
    path="",
    response_model=Event
)
async def create_event(event: EventCreateRequest):
    new_event: Event = await create_new_event(event)
    return new_event

@router.get(
    path="",
    response_model=EventsGetResponse
)
async def get_all_events():
    events = await get_events()
    return EventsGetResponse(events=events)

@router.get(
    path="/{event_id}",
    response_model=Event
)
async def get_event(event_id: int):
    event: Event = await get_event_by_id(event_id)
    return event

@router.patch(
    path='/{event_id}',
    response_model = Event
)
async def update_event(event_id: int, status: EventUpdateRequest):
    updated_event: Event = await update_event_status(event_id, status)
    return updated_event

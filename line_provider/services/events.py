import time

import httpx
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from line_provider.config import settings

from ..schemas.events import Event, EventCreateRequest, EventUpdateRequest, EventState
from ..utils.events_data import events


async def check_event_exist(event_id: int) -> bool:
    return str(event_id) in events.keys()


async def create_new_event(event: EventCreateRequest) -> Event:
    if await check_event_exist(event.event_id):
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"Event with id {event.event_id} already exist")
    events[str(event.event_id)] = event
    return event


async def get_events() -> list[Event]:
    all_events = list(e for e in events.values() if time.time() < e.deadline and e.state == EventState.NEW)
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

    await send_webhook(event_id, status.state.value)

    return event


async def send_webhook(event_id: int, status: int) -> None:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.BET_MAKER_URL}/bets/webhook",
            json={
                "event_id": event_id,
                "status": status,
            })

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to notify bet-maker")

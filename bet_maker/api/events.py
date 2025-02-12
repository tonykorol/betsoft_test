from fastapi import APIRouter

from bet_maker.schemas.events import GetAvailableEventsResponse
from bet_maker.services.events import get_available_events

router = APIRouter(prefix="/events", tags=["Events"])

@router.get(
    path="",
    response_model=GetAvailableEventsResponse
)
async def get_all_events():
    events = await get_available_events()
    return events
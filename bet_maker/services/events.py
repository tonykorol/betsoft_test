import httpx

from bet_maker.config import settings


async def get_available_events() -> list:
    url = f"{settings.LINE_PROVIDER_URL}/events"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()

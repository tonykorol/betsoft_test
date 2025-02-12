from fastapi import FastAPI

from bet_maker.api.events import router as events_router
from bet_maker.api.bets import router as bets_router

app = FastAPI()

app.include_router(events_router)
app.include_router(bets_router)

@app.get('/health_check')
async def health_check():
    return {"status": "ok"}

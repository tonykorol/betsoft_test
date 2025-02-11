from fastapi import FastAPI

from .api.event import router as events_router


app = FastAPI()

app.include_router(events_router)

@app.get("/health_check")
async def health_check():
    return {"status": "ok"}

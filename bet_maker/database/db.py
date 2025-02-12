from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from bet_maker.config import settings

DATABASE_URL = settings.DB_URL


engine = create_async_engine(DATABASE_URL)
AsyncSession = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncSession:
    async with AsyncSession() as session:
        yield session

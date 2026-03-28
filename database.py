from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Using aiosqlite for async support with SQLite
DATABASE_URL = "sqlite+aiosqlite:///./crisisaseessment.db"

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

# Dependency to be used in FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

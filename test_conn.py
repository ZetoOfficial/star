import asyncio

from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import load_settings

settings = load_settings()

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
    settings.postgres.user,
    settings.postgres.password,
    settings.postgres.host,
    settings.postgres.port,
    settings.postgres.database,
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=1800)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def ping_database():
    while True:
        try:
            async with SessionLocal() as session:
                result = await session.execute(text("SELECT 1"))
                print(f"Database responded: {result.fetchone()}")
        except OperationalError:
            print("Database connection failed.")
        await asyncio.sleep(1)


asyncio.run(ping_database())

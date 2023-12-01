from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models import (
    Star as ORMStar,
    Universe as ORMUniverse,
    Galaxy as ORMGalaxy,
)


class ReportRepository:
    @staticmethod
    async def get_report_data(universe_id: UUID):
        async with SessionLocal() as session:
            session: AsyncSession

            universe_query = select(ORMUniverse).where(ORMUniverse.id == universe_id)
            universe_result = await session.execute(universe_query)
            universe = universe_result.scalars().first()
            if universe is None:
                raise Exception("Universe not found")

            galaxy_query = select(ORMGalaxy).where(ORMGalaxy.universe_id == universe_id)
            galaxy_result = await session.execute(galaxy_query)
            galaxies = galaxy_result.scalars().all()

            star_query = (
                select(ORMStar)
                .join(ORMGalaxy)
                .where(ORMGalaxy.universe_id == universe_id)
                .options(selectinload(ORMStar.planet))
            )
            star_result = await session.execute(star_query)
            stars = star_result.scalars().all()

            report_data = {
                "universe": universe,
                "galaxies": galaxies,
                "stars": stars,
            }

            return report_data

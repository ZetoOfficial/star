from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models import (
    Star as ORMStar,
    Galaxy as ORMGalaxy,
)


class ReportRepository:
    @staticmethod
    async def get_report_data(galaxy_id: UUID):
        async with SessionLocal() as session:
            session: AsyncSession

            galaxy_query = select(ORMGalaxy).where(ORMGalaxy.id == galaxy_id)
            galaxy_result = await session.execute(galaxy_query)
            galaxy = galaxy_result.scalars().first()
            if galaxy is None:
                raise Exception("Galaxy not found")

            star_query = (
                select(ORMStar)
                .join(ORMGalaxy)
                .where(ORMGalaxy.id == galaxy_id)
                .options(selectinload(ORMStar.planet))
            )
            star_result = await session.execute(star_query)
            stars = star_result.scalars().all()

            plantes = []
            for star in stars:
                if star.planet:
                    plantes += star.planet

            report_data = {
                "galaxy": galaxy,
                "stars": stars,
                "planets": plantes,
            }

            return report_data

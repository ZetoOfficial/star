from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models.star_constellation import StarConstellation as ORMStarConstellation
from app.schemas import StarConstellationDTO

from .errors import NotFoundException


class CRUDStarConstellation:
    @staticmethod
    async def create_star_constellation(dto: StarConstellationDTO) -> StarConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMStarConstellation(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
        return StarConstellationDTO.model_validate(orm_obj)

    @staticmethod
    async def get_star_constellation(star_id: UUID, constellation_id: UUID) -> StarConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMStarConstellation).where(
                ORMStarConstellation.star_id == star_id,
                ORMStarConstellation.constellation_id == constellation_id)
            result = await session.execute(query)
            star_constellation = result.scalar_one_or_none()
            if star_constellation is None:
                raise NotFoundException("StarConstellation not found")
        return StarConstellationDTO.model_validate(star_constellation)

    @staticmethod
    async def delete_star_constellation(star_id: UUID, constellation_id: UUID) -> None:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMStarConstellation).where(
                ORMStarConstellation.star_id == star_id,
                ORMStarConstellation.constellation_id == constellation_id)
            await session.execute(query)
            await session.commit()

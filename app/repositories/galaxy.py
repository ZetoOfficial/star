from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models.galaxy import Galaxy as ORMGalaxy
from app.schemas import GalaxyDTO, InputGalaxyDTO

from .errors import NotFoundException


class CRUDGalaxy:
    @staticmethod
    async def create_galaxy(dto: InputGalaxyDTO) -> GalaxyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMGalaxy(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
        return GalaxyDTO.model_validate(orm_obj)

    @staticmethod
    async def get_all_galaxies(limit: int = None, offset: int = None) -> list[GalaxyDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMGalaxy)
            if limit is not None:
                query = query.limit(limit)
            if offset is not None:
                query = query.offset(offset)
            result = await session.execute(query)
            galaxies = result.scalars().all()
        return [GalaxyDTO.model_validate(galaxy) for galaxy in galaxies]

    @staticmethod
    async def get_galaxy_by_id(galaxy_id: UUID) -> GalaxyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMGalaxy).where(ORMGalaxy.id == galaxy_id)
            result = await session.execute(query)
            galaxy = result.scalar_one_or_none()
            if galaxy is None:
                return NotFoundException("Galaxy not found")
        return GalaxyDTO.model_validate(galaxy)

    @staticmethod
    async def update_galaxy(galaxy_id: UUID, dto: InputGalaxyDTO) -> GalaxyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                update(ORMGalaxy)
                .where(ORMGalaxy.id == galaxy_id)
                .values(**dto.model_dump())
                .returning(ORMGalaxy)
            )
            result = await session.execute(query)
            await session.commit()
            galaxy = result.one()
        return GalaxyDTO.model_validate(galaxy)

    @staticmethod
    async def delete_galaxy(galaxy_id: UUID) -> None:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMGalaxy).where(ORMGalaxy.id == galaxy_id)
            await session.execute(query)
            await session.commit()

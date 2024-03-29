from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models.planet import Planet as ORMPlanet
from app.schemas import PlanetDTO, InputPlanetDTO
from .errors import NotFoundException


class CRUDPlanet:
    @staticmethod
    async def create_planet(dto: InputPlanetDTO) -> PlanetDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMPlanet(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
            return await CRUDPlanet.get_planet_by_id(orm_obj.id)

    @staticmethod
    async def get_all_planets(limit: int = None, offset: int = None) -> list[PlanetDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMPlanet).options(selectinload(ORMPlanet.star))
            if limit is not None:
                query = query.limit(limit)
            if offset is not None:
                query = query.offset(offset)
            result = await session.execute(query)
            planets = result.scalars().all()
            return planets

    @staticmethod
    async def get_planet_by_id(planet_id: UUID) -> PlanetDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                select(ORMPlanet)
                .where(ORMPlanet.id == planet_id)
                .options(selectinload(ORMPlanet.star))
            )
            result = await session.execute(query)
            planet = result.scalar_one_or_none()
            if planet is None:
                raise NotFoundException("Planet not found")
            return planet

    @staticmethod
    async def update_planet(planet_id: UUID, dto: InputPlanetDTO) -> PlanetDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                update(ORMPlanet)
                .where(ORMPlanet.id == planet_id)
                .values(**dto.model_dump())
                .returning(ORMPlanet)
            )
            await session.execute(query)
            await session.commit()
            return await CRUDPlanet.get_planet_by_id(planet_id)

    @staticmethod
    async def delete_planet(planet_id: UUID) -> None:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMPlanet).where(ORMPlanet.id == planet_id)
            await session.execute(query)
            await session.commit()

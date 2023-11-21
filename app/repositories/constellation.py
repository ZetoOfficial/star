from sqlalchemy import delete, select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models.constellation import Constellation as ORMConstellation
from app.models.galaxy import Galaxy as ORMGalaxy
from app.models.star_constellation import StarConstellation as ORMStarConstellation
from app.schemas import ConstellationDTO, InputConstellationDTO

from .errors import NotFoundException


class CRUDConstellation:
    @staticmethod
    async def create_constellation(dto: InputConstellationDTO) -> ConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMConstellation(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
        return orm_obj

    @staticmethod
    async def get_all_constellations(limit: int, offset: int) -> list[ConstellationDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMConstellation)
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            query = query.options(selectinload(ORMConstellation.galaxy))
            query = query.options(selectinload(ORMConstellation.star_constellation))
            result = await session.execute(query)
        return result.scalars().all()

    @staticmethod
    async def get_constellation_by_id(_id: int) -> ConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMConstellation).where(ORMConstellation.id == _id)
            result = await session.execute(query)
            if result is None:
                return NotFoundException(f"Constellation with id {_id} not found")
        return result.scalar_one()

    @staticmethod
    async def update_constellation(_id: int, dto: InputConstellationDTO) -> ConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                update(ORMConstellation)
                .where(ORMConstellation.id == id)
                .values(**dto.model_dump())
                .returning(ORMConstellation)
            )
            result = await session.execute(query)
            await session.commit()
        return result.scalar_one()

    @staticmethod
    async def delete_constellation(_id: int) -> bool:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMConstellation).where(ORMConstellation.id == _id)
            await session.execute(query)
            await session.commit()
        return True

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database import SessionLocal
from app.models.constellation import Constellation as ORMConstellation
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
            return await CRUDConstellation.get_constellation_by_id(orm_obj.id)

    @staticmethod
    async def get_all_constellations(limit: int, offset: int) -> list[ConstellationDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMConstellation).options(
                joinedload(ORMConstellation.galaxy)
            )
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            result = await session.execute(query)
            constellations = result.scalars().all()
            return constellations

    @staticmethod
    async def get_constellation_by_id(_id: int) -> ConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                select(ORMConstellation)
                .where(ORMConstellation.id == _id)
                .options(
                    joinedload(ORMConstellation.galaxy),
                )
            )
            result = await session.execute(query)
            if result is None:
                raise NotFoundException(f"Constellation with id {_id} not found")
            return result.scalar_one()

    @staticmethod
    async def update_constellation(
        _id: int, dto: InputConstellationDTO
    ) -> ConstellationDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                update(ORMConstellation)
                .where(ORMConstellation.id == _id)
                .values(**dto.model_dump())
                .returning(ORMConstellation)
            )
            await session.execute(query)
            await session.commit()
            return await CRUDConstellation.get_constellation_by_id(_id)

    @staticmethod
    async def delete_constellation(_id: int) -> bool:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMConstellation).where(ORMConstellation.id == _id)
            await session.execute(query)
            await session.commit()
            return True

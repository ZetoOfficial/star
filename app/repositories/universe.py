from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models.universe import Universe as ORMUniverse
from app.schemas import UniverseDTO, InputUniverseDTO
from .errors import NotFoundException


class CRUDUniverse:
    @staticmethod
    async def create_universe(dto: InputUniverseDTO) -> UniverseDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMUniverse(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
        return UniverseDTO.model_validate(orm_obj)

    @staticmethod
    async def get_all_universes(limit: int = None, offset: int = None) -> list[UniverseDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMUniverse)
            if limit is not None:
                query = query.limit(limit)
            if offset is not None:
                query = query.offset(offset)
            result = await session.execute(query)
            universes = result.scalars().all()
        return [UniverseDTO.model_validate(universe) for universe in universes]

    @staticmethod
    async def get_universe_by_id(universe_id: UUID) -> UniverseDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMUniverse).where(ORMUniverse.id == universe_id)
            result = await session.execute(query)
            universe = result.scalar_one_or_none()
            if universe is None:
                raise NotFoundException("Universe not found")
        return UniverseDTO.model_validate(universe)

    @staticmethod
    async def update_universe(universe_id: UUID, dto: InputUniverseDTO) -> UniverseDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                update(ORMUniverse)
                .where(ORMUniverse.id == universe_id)
                .values(**dto.model_dump())
                .returning(ORMUniverse)
            )
            result = await session.execute(query)
            await session.commit()
            universe = result.one()
        return UniverseDTO.model_validate(universe)

    @staticmethod
    async def delete_universe(universe_id: UUID) -> None:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMUniverse).where(ORMUniverse.id == universe_id)
            await session.execute(query)
            await session.commit()

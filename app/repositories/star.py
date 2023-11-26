from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models.star import Star as ORMStar
from app.schemas import StarDTO, InputStarDTO
from .errors import NotFoundException


class CRUDStar:
    @staticmethod
    async def create_star(dto: InputStarDTO) -> StarDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMStar(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
            return await CRUDStar.get_star_by_id(orm_obj.id)

    @staticmethod
    async def get_all_stars(limit: int = None, offset: int = None) -> list[StarDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMStar)
            query = query.options(selectinload(ORMStar.galaxy))
            if limit is not None:
                query = query.limit(limit)
            if offset is not None:
                query = query.offset(offset)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_star_by_id(star_id: UUID) -> StarDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMStar).where(ORMStar.id == star_id)
            query = query.options(selectinload(ORMStar.galaxy))
            result = await session.execute(query)
            star = result.scalar_one_or_none()
            if star is None:
                raise NotFoundException("Star not found")
            return star

    @staticmethod
    async def update_star(star_id: UUID, dto: InputStarDTO) -> StarDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                update(ORMStar)
                .where(ORMStar.id == star_id)
                .values(**dto.model_dump())
                .returning(ORMStar)
            )
            await session.execute(query)
            await session.commit()
            return await CRUDStar.get_star_by_id(star_id)

    @staticmethod
    async def delete_star(star_id: UUID) -> None:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMStar).where(ORMStar.id == star_id)
            await session.execute(query)
            await session.commit()

from uuid import UUID

from app.repositories import CRUDStar
from app.schemas import StarDTO, InputStarDTO


class StarService:
    @staticmethod
    async def create_star(dto: InputStarDTO) -> StarDTO:
        return await CRUDStar.create_star(dto)

    @staticmethod
    async def get_all_stars(limit: int, offset: int) -> list[StarDTO]:
        return await CRUDStar.get_all_stars(limit, offset)

    @staticmethod
    async def get_star_by_id(star_id: UUID) -> StarDTO:
        return await CRUDStar.get_star_by_id(star_id)

    @staticmethod
    async def update_star(star_id: UUID, dto: InputStarDTO) -> StarDTO:
        return await CRUDStar.update_star(star_id, dto)

    @staticmethod
    async def delete_star(star_id: UUID) -> None:
        return await CRUDStar.delete_star(star_id)

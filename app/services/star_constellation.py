from uuid import UUID

from app.repositories import CRUDStarConstellation
from app.schemas import StarConstellationDTO


class StarConstellationService:
    @staticmethod
    async def create_star_constellation(dto: StarConstellationDTO) -> StarConstellationDTO:
        return await CRUDStarConstellation.create_star_constellation(dto)

    @staticmethod
    async def get_star_constellation(star_id: UUID, constellation_id: UUID) -> StarConstellationDTO:
        return await CRUDStarConstellation.get_star_constellation(star_id, constellation_id)

    @staticmethod
    async def delete_star_constellation(star_id: UUID, constellation_id: UUID) -> None:
        return await CRUDStarConstellation.delete_star_constellation(star_id, constellation_id)

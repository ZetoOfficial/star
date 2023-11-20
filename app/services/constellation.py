from uuid import UUID

from app.repositories import CRUDConstellation
from app.schemas import ConstellationDTO, InputConstellationDTO


class ConstellationService:
    @staticmethod
    async def create_constellation(dto: InputConstellationDTO) -> ConstellationDTO:
        return await CRUDConstellation.create_constellation(dto)

    @staticmethod
    async def get_all_constellations(limit: int = None, offset: int = None) -> list[ConstellationDTO]:
        return await CRUDConstellation.get_all_constellations(limit, offset)

    @staticmethod
    async def get_constellation_by_id(galaxy_id: UUID) -> ConstellationDTO:
        return await CRUDConstellation.get_constellation_by_id(galaxy_id)

    @staticmethod
    async def update_constellation(galaxy_id: UUID, dto: InputConstellationDTO) -> ConstellationDTO:
        return await CRUDConstellation.update_constellation(galaxy_id, dto)

    @staticmethod
    async def delete_constellation(galaxy_id: UUID) -> None:
        return await CRUDConstellation.delete_constellation(galaxy_id)

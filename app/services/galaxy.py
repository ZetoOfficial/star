from uuid import UUID

from app.repositories import CRUDGalaxy
from app.schemas import GalaxyDTO, InputGalaxyDTO


class GalaxyService:
    @staticmethod
    async def create_galaxy(dto: InputGalaxyDTO) -> GalaxyDTO:
        return await CRUDGalaxy.create_galaxy(dto)

    @staticmethod
    async def get_all_galaxies(limit: int = None, offset: int = None) -> list[GalaxyDTO]:
        return await CRUDGalaxy.get_all_galaxies(limit, offset)

    @staticmethod
    async def get_galaxy_by_id(galaxy_id: UUID) -> GalaxyDTO:
        return await CRUDGalaxy.get_galaxy_by_id(galaxy_id)

    @staticmethod
    async def update_galaxy(galaxy_id: UUID, dto: InputGalaxyDTO) -> GalaxyDTO:
        return await CRUDGalaxy.update_galaxy(galaxy_id, dto)

    @staticmethod
    async def delete_galaxy(galaxy_id: UUID) -> None:
        return await CRUDGalaxy.delete_galaxy(galaxy_id)

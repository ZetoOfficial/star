from uuid import UUID

from app.repositories import CRUDUniverse
from app.schemas import UniverseDTO, InputUniverseDTO


class UniverseService:
    @staticmethod
    async def create_universe(dto: InputUniverseDTO) -> UniverseDTO:
        return await CRUDUniverse.create_universe(dto)

    @staticmethod
    async def get_all_universes(limit: int, offset: int) -> list[UniverseDTO]:
        return await CRUDUniverse.get_all_universes(limit, offset)

    @staticmethod
    async def get_universe_by_id(universe_id: UUID) -> UniverseDTO:
        return await CRUDUniverse.get_universe_by_id(universe_id)

    @staticmethod
    async def update_universe(universe_id: UUID, dto: InputUniverseDTO) -> UniverseDTO:
        return await CRUDUniverse.update_universe(universe_id, dto)

    @staticmethod
    async def delete_universe(universe_id: UUID) -> None:
        return await CRUDUniverse.delete_universe(universe_id)

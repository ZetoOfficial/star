from uuid import UUID
from app.repositories.planet import CRUDPlanet
from app.schemas import PlanetDTO, InputPlanetDTO


class PlanetService:
    @staticmethod
    async def create_planet(dto: InputPlanetDTO) -> PlanetDTO:
        return await CRUDPlanet.create_planet(dto)

    @staticmethod
    async def get_all_planets(limit: int, offset: int) -> list[PlanetDTO]:
        return await CRUDPlanet.get_all_planets(limit, offset)

    @staticmethod
    async def get_planet_by_id(planet_id: UUID) -> PlanetDTO:
        return await CRUDPlanet.get_planet_by_id(planet_id)

    @staticmethod
    async def update_planet(planet_id: UUID, dto: InputPlanetDTO) -> PlanetDTO:
        return await CRUDPlanet.update_planet(planet_id, dto)

    @staticmethod
    async def delete_planet(planet_id: UUID) -> None:
        return await CRUDPlanet.delete_planet(planet_id)

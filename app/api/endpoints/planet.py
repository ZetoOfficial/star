from fastapi import APIRouter
from app.schemas import PlanetDTO, InputPlanetDTO
from app.services import PlanetService
from uuid import UUID

planet_router = APIRouter()


@planet_router.post("/planets", response_model=PlanetDTO)
async def create_planet(dto: InputPlanetDTO):
    """Create a new planet in the database"""
    return await PlanetService.create_planet(dto)


@planet_router.get("/planets", response_model=list[PlanetDTO])
async def get_all_planets(limit: int = 100, offset: int = 0):
    """Get all planets from the database"""
    return await PlanetService.get_all_planets(limit, offset)


@planet_router.get("/planets/{planet_id}", response_model=PlanetDTO)
async def get_planet_by_id(planet_id: UUID):
    """Get a specific planet by its ID"""
    return await PlanetService.get_planet_by_id(planet_id)


@planet_router.put("/planets/{planet_id}", response_model=PlanetDTO)
async def update_planet(planet_id: UUID, dto: InputPlanetDTO):
    """Update a specific planet"""
    return await PlanetService.update_planet(planet_id, dto)


@planet_router.delete("/planets/{planet_id}", response_model=None)
async def delete_planet(planet_id: UUID):
    """Delete a specific planet"""
    await PlanetService.delete_planet(planet_id)
    return {"message": "Planet deleted successfully"}

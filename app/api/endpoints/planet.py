from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.repositories.errors import NotFoundException
from app.schemas import PlanetDTO, InputPlanetDTO
from app.services import PlanetService

planet_router = APIRouter()


@planet_router.post("/planets", response_model=PlanetDTO)
async def create_planet(dto: InputPlanetDTO):
    """Create a new planet in the database"""
    try:
        return await PlanetService.create_planet(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@planet_router.get("/planets", response_model=list[PlanetDTO])
async def get_all_planets(limit: int = 100, offset: int = 0):
    """Get all planets from the database"""
    try:
        return await PlanetService.get_all_planets(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@planet_router.get("/planets/{planet_id}", response_model=PlanetDTO)
async def get_planet_by_id(planet_id: UUID):
    """Get a specific planet by its ID"""
    try:
        return await PlanetService.get_planet_by_id(planet_id)
    except NotFoundException:
        raise HTTPException(status_code=404, detail="Planet not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@planet_router.put("/planets/{planet_id}", response_model=PlanetDTO)
async def update_planet(planet_id: UUID, dto: InputPlanetDTO):
    """Update a specific planet"""
    try:
        return await PlanetService.update_planet(planet_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@planet_router.delete("/planets/{planet_id}", response_model=None)
async def delete_planet(planet_id: UUID):
    """Delete a specific planet"""
    try:
        await PlanetService.delete_planet(planet_id)
        return {"message": "Planet deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

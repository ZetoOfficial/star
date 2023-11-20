from fastapi import APIRouter
from app.schemas import GalaxyDTO, InputGalaxyDTO
from app.services import GalaxyService
from uuid import UUID

galaxy_router = APIRouter()


@galaxy_router.post("/galaxies", response_model=GalaxyDTO)
async def create_galaxy(dto: InputGalaxyDTO):
    """Create a new galaxy in the database"""
    return await GalaxyService.create_galaxy(dto)


@galaxy_router.get("/galaxies", response_model=list[GalaxyDTO])
async def get_all_galaxies(limit: int = 100, offset: int = 0):
    """Get all galaxies from the database"""
    return await GalaxyService.get_all_galaxies(limit, offset)


@galaxy_router.get("/galaxies/{galaxy_id}", response_model=GalaxyDTO)
async def get_galaxy_by_id(galaxy_id: UUID):
    """Get a specific galaxy by its ID"""
    return await GalaxyService.get_galaxy_by_id(galaxy_id)


@galaxy_router.put("/galaxies/{galaxy_id}", response_model=GalaxyDTO)
async def update_galaxy(galaxy_id: UUID, dto: InputGalaxyDTO):
    """Update a specific galaxy"""
    return await GalaxyService.update_galaxy(galaxy_id, dto)


@galaxy_router.delete("/galaxies/{galaxy_id}", response_model=None)
async def delete_galaxy(galaxy_id: UUID):
    """Delete a specific galaxy"""
    await GalaxyService.delete_galaxy(galaxy_id)
    return {"message": "Galaxy deleted successfully"}

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import GalaxyDTO, InputGalaxyDTO
from app.services import GalaxyService

galaxy_router = APIRouter()


@galaxy_router.post("/galaxies", response_model=GalaxyDTO)
async def create_galaxy(dto: InputGalaxyDTO):
    """Create a new galaxy in the database"""
    try:
        return await GalaxyService.create_galaxy(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@galaxy_router.get("/galaxies", response_model=list[GalaxyDTO])
async def get_all_galaxies(limit: int = 100, offset: int = 0):
    """Get all galaxies from the database"""
    try:
        return await GalaxyService.get_all_galaxies(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@galaxy_router.get("/galaxies/{galaxy_id}", response_model=GalaxyDTO)
async def get_galaxy_by_id(galaxy_id: UUID):
    """Get a specific galaxy by its ID"""
    try:
        return await GalaxyService.get_galaxy_by_id(galaxy_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@galaxy_router.put("/galaxies/{galaxy_id}", response_model=GalaxyDTO)
async def update_galaxy(galaxy_id: UUID, dto: InputGalaxyDTO):
    """Update a specific galaxy"""
    try:
        return await GalaxyService.update_galaxy(galaxy_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@galaxy_router.delete("/galaxies/{galaxy_id}", response_model=None)
async def delete_galaxy(galaxy_id: UUID):
    """Delete a specific galaxy"""
    try:
        await GalaxyService.delete_galaxy(galaxy_id)
        return {"message": "Galaxy deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

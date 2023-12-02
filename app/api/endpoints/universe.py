from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import UniverseDTO, InputUniverseDTO
from app.services import UniverseService

universe_router = APIRouter()


@universe_router.post("/universes", response_model=UniverseDTO)
async def create_universe(dto: InputUniverseDTO):
    """Create a new universe in the database"""
    try:
        return await UniverseService.create_universe(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@universe_router.get("/universes", response_model=list[UniverseDTO])
async def get_all_universes(limit: int = 100, offset: int = 0):
    """Get all universes from the database"""
    try:
        return await UniverseService.get_all_universes(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@universe_router.get("/universes/{universe_id}", response_model=UniverseDTO)
async def get_universe_by_id(universe_id: UUID):
    """Get a specific universe by its ID"""
    try:
        return await UniverseService.get_universe_by_id(universe_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@universe_router.put("/universes/{universe_id}", response_model=UniverseDTO)
async def update_universe(universe_id: UUID, dto: InputUniverseDTO):
    """Update a specific universe"""
    try:
        return await UniverseService.update_universe(universe_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@universe_router.delete("/universes/{universe_id}", response_model=None)
async def delete_universe(universe_id: UUID):
    """Delete a specific universe"""
    try:
        await UniverseService.delete_universe(universe_id)
        return {"message": "Universe deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

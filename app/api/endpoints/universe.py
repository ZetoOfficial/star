from fastapi import APIRouter
from app.schemas import UniverseDTO, InputUniverseDTO
from app.services import UniverseService
from uuid import UUID

universe_router = APIRouter()


@universe_router.post("/universes", response_model=UniverseDTO)
async def create_universe(dto: InputUniverseDTO):
    """Create a new universe in the database"""
    return await UniverseService.create_universe(dto)


@universe_router.get("/universes", response_model=list[UniverseDTO])
async def get_all_universes(limit: int = 100, offset: int = 0):
    """Get all universes from the database"""
    return await UniverseService.get_all_universes(limit, offset)


@universe_router.get("/universes/{universe_id}", response_model=UniverseDTO)
async def get_universe_by_id(universe_id: UUID):
    """Get a specific universe by its ID"""
    return await UniverseService.get_universe_by_id(universe_id)


@universe_router.put("/universes/{universe_id}", response_model=UniverseDTO)
async def update_universe(universe_id: UUID, dto: InputUniverseDTO):
    """Update a specific universe"""
    return await UniverseService.update_universe(universe_id, dto)


@universe_router.delete("/universes/{universe_id}", response_model=None)
async def delete_universe(universe_id: UUID):
    """Delete a specific universe"""
    await UniverseService.delete_universe(universe_id)
    return {"message": "Universe deleted successfully"}

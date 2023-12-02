from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import ConstellationDTO, InputConstellationDTO
from app.services import ConstellationService

constellation_router = APIRouter()


@constellation_router.post("/constellations", response_model=ConstellationDTO)
async def create_constellation(dto: InputConstellationDTO):
    """Create a new constellation in the database"""
    try:
        return await ConstellationService.create_constellation(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@constellation_router.get("/constellations", response_model=list[ConstellationDTO])
async def get_all_constellations(limit: int = 100, offset: int = 0):
    """Get all constellations from the database"""
    try:
        return await ConstellationService.get_all_constellations(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@constellation_router.get(
    "/constellations/{constellation_id}", response_model=ConstellationDTO
)
async def get_constellation_by_id(constellation_id: UUID):
    """Get a specific constellation by its ID"""
    try:
        return await ConstellationService.get_constellation_by_id(constellation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@constellation_router.put(
    "/constellations/{constellation_id}", response_model=ConstellationDTO
)
async def update_constellation(constellation_id: UUID, dto: InputConstellationDTO):
    """Update a specific constellation"""
    try:
        return await ConstellationService.update_constellation(constellation_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@constellation_router.delete("/constellations/{constellation_id}", response_model=None)
async def delete_constellation(constellation_id: UUID):
    """Delete a specific constellation"""
    try:
        await ConstellationService.delete_constellation(constellation_id)
        return {"message": "Constellation deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import StarDTO, InputStarDTO
from app.services import StarService

star_router = APIRouter()


@star_router.post("/stars", response_model=StarDTO)
async def create_star(dto: InputStarDTO):
    """Create a new star in the database"""
    try:
        return await StarService.create_star(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@star_router.get("/stars", response_model=list[StarDTO])
async def get_all_stars(limit: int = 100, offset: int = 0):
    """Get all stars from the database"""
    try:
        return await StarService.get_all_stars(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@star_router.get("/stars/{star_id}", response_model=StarDTO)
async def get_star_by_id(star_id: UUID):
    """Get a specific star by its ID"""
    try:
        return await StarService.get_star_by_id(star_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@star_router.put("/stars/{star_id}", response_model=StarDTO)
async def update_star(star_id: UUID, dto: InputStarDTO):
    """Update a specific star"""
    try:
        return await StarService.update_star(star_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@star_router.delete("/stars/{star_id}", response_model=None)
async def delete_star(star_id: UUID):
    """Delete a specific star"""
    try:
        await StarService.delete_star(star_id)
        return {"message": "Star deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter
from app.schemas import StarDTO, InputStarDTO
from app.services import StarService
from uuid import UUID

star_router = APIRouter()


@star_router.post("/stars", response_model=StarDTO)
async def create_star(dto: InputStarDTO):
    """Create a new star in the database"""
    return await StarService.create_star(dto)


@star_router.get("/stars", response_model=list[StarDTO])
async def get_all_stars(limit: int = 100, offset: int = 0):
    """Get all stars from the database"""
    return await StarService.get_all_stars(limit, offset)


@star_router.get("/stars/{star_id}", response_model=StarDTO)
async def get_star_by_id(star_id: UUID):
    """Get a specific star by its ID"""
    return await StarService.get_star_by_id(star_id)


@star_router.put("/stars/{star_id}", response_model=StarDTO)
async def update_star(star_id: UUID, dto: InputStarDTO):
    """Update a specific star"""
    return await StarService.update_star(star_id, dto)


@star_router.delete("/stars/{star_id}", response_model=None)
async def delete_star(star_id: UUID):
    """Delete a specific star"""
    await StarService.delete_star(star_id)
    return {"message": "Star deleted successfully"}

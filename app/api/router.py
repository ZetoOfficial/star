from fastapi import APIRouter

from .endpoints import (
    universe_router,
    planet_router,
    galaxy_router,
    star_router,
    constellation_router,
    report_router,
    audit_router,
)

api_router = APIRouter()

api_router.include_router(constellation_router, tags=["constellation"])
api_router.include_router(universe_router, tags=["universe"])
api_router.include_router(planet_router, tags=["planet"])
api_router.include_router(galaxy_router, tags=["galaxy"])
api_router.include_router(star_router, tags=["star"])
api_router.include_router(report_router, tags=["reports"])
api_router.include_router(audit_router, tags=["audit"])

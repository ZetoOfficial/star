from datetime import time
from pydantic import BaseModel, UUID4
from typing import Optional


class PlanetDTO(BaseModel):
    id: UUID4
    name: str
    mass: float
    diameter: float
    distance_from_star: float
    orbital_period: Optional[time]
    surface_temperature: Optional[float]
    star_id: UUID4


class InputPlanetDTO(BaseModel):
    name: str
    mass: float
    diameter: float
    distance_from_star: float
    orbital_period: Optional[time]
    surface_temperature: Optional[float]
    star_id: UUID4

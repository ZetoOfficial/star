from typing import Optional

from pydantic import BaseModel, UUID4


class StarShortDTO(BaseModel):
    id: UUID4
    name: str


class PlanetDTO(BaseModel):
    id: UUID4
    name: str
    mass: float
    diameter: float
    distance_from_star: float
    surface_temperature: Optional[float]
    star: StarShortDTO


class InputPlanetDTO(BaseModel):
    name: str
    mass: float
    diameter: float
    distance_from_star: float
    surface_temperature: Optional[float]
    star_id: UUID4

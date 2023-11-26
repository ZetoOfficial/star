from pydantic import BaseModel, UUID4
from .galaxy_dto import GalaxyDTO


class GalaxyShortDTO(BaseModel):
    id: UUID4
    name: str


class StarDTO(BaseModel):
    id: UUID4
    name: str
    spectral_type: str
    luminosity: float
    distance_from_earth: float
    temperature: float

    galaxy: GalaxyShortDTO


class InputStarDTO(BaseModel):
    name: str
    galaxy_id: UUID4
    spectral_type: str
    luminosity: float
    distance_from_earth: float
    temperature: float

from pydantic import BaseModel, UUID4
from typing import Optional
from .universe_dto import UniverseDTO


class GalaxyDTO(BaseModel):
    id: UUID4
    name: str
    size: float
    shape: Optional[str]
    composition: Optional[str]
    distance_from_earth: Optional[float]
    universe: Optional[UniverseDTO]


class InputGalaxyDTO(BaseModel):
    name: str
    universe_id: Optional[UUID4]
    size: float
    shape: Optional[str]
    composition: Optional[str]
    distance_from_earth: Optional[float]

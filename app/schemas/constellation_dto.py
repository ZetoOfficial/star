from pydantic import BaseModel, UUID4
from typing import Optional
from .galaxy_dto import GalaxyDTO
from .star_constellation_dto import StarConstellationDTO


class ConstellationDTO(BaseModel):
    id: UUID4
    galaxy_id: UUID4
    name: str
    shape: Optional[str]
    abbreviation: Optional[str]
    history: Optional[str]

    galaxy: GalaxyDTO
    star_constellation: list[StarConstellationDTO]


class InputConstellationDTO(BaseModel):
    galaxy_id: UUID4
    name: str
    shape: Optional[str]
    abbreviation: Optional[str]
    history: Optional[str]

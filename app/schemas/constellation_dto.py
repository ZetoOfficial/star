from typing import Optional

from pydantic import BaseModel, UUID4


class GalaxyShortDTO(BaseModel):
    id: UUID4
    name: str


class StarShortDTO(BaseModel):
    id: UUID4
    name: str


class ConstellationDTO(BaseModel):
    id: UUID4
    name: str
    shape: Optional[str]
    abbreviation: Optional[str]
    history: Optional[str]

    galaxy: GalaxyShortDTO


class InputConstellationDTO(BaseModel):
    galaxy_id: UUID4
    name: str
    shape: Optional[str]
    abbreviation: Optional[str]
    history: Optional[str]

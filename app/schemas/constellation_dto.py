from pydantic import BaseModel, UUID4
from typing import Optional


class ConstellationDTO(BaseModel):
    id: UUID4
    galaxy_id: UUID4
    name: str
    shape: Optional[str]
    abbreviation: Optional[str]
    history: Optional[str]


class InputConstellationDTO(BaseModel):
    galaxy_id: UUID4
    name: str
    shape: Optional[str]
    abbreviation: Optional[str]
    history: Optional[str]

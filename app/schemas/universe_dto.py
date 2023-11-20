from pydantic import BaseModel, UUID4
from typing import Optional


class UniverseDTO(BaseModel):
    id: UUID4
    name: str
    size: float
    composition: Optional[str]


class InputUniverseDTO(BaseModel):
    name: str
    size: float
    composition: Optional[str]

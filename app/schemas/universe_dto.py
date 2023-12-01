from typing import Optional

from pydantic import BaseModel, UUID4


class UniverseDTO(BaseModel):
    id: UUID4
    name: str
    size: float
    composition: Optional[str]


class InputUniverseDTO(BaseModel):
    name: str
    size: float
    composition: Optional[str]

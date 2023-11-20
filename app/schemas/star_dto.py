from pydantic import BaseModel, UUID4


class StarDTO(BaseModel):
    id: UUID4
    name: str
    galaxy_id: UUID4
    spectral_type: str
    luminosity: float
    distance_from_earth: float
    temperature: float


class InputStarDTO(BaseModel):
    name: str
    galaxy_id: UUID4
    spectral_type: str
    luminosity: float
    distance_from_earth: float
    temperature: float

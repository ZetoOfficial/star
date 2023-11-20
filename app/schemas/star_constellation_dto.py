from pydantic import BaseModel, UUID4


class StarConstellationDTO(BaseModel):
    star_id: UUID4
    constellation_id: UUID4

from pydantic import BaseModel


class ReportDTO(BaseModel):
    name: str
    link: str


class GalaxyReportDTO(BaseModel):
    name: str
    shape: str
    size: float
    stars: list[str]
    planets: list[str]
    composition: str

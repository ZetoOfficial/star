from datetime import datetime

from pydantic import BaseModel


class CreateReportDTO(BaseModel):
    report_type: str
    date_from: datetime
    date_to: datetime


class ReportDTO(BaseModel):
    name: str
    link: str

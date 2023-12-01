from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional


class AuditDTO(BaseModel):
    id: int
    operation_type: str
    table_name: str
    row_id: UUID4
    old_value: Optional[str]
    new_value: Optional[str]
    timestamp: datetime

    class Config:
        orm_mode = True

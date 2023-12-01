from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Audit(Base):
    __tablename__ = "audit"

    id = Column(Integer, primary_key=True)
    table_name = Column(String(256), nullable=False)
    row_id = Column(UUID(as_uuid=True))
    old_value = Column(Text)
    new_value = Column(Text)
    operation_type = Column(String(10))  # INSERT, UPDATE, DELETE
    timestamp = Column(DateTime, default=datetime.utcnow)

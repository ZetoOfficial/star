import uuid

from sqlalchemy import Column, Float, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from . import Base


class Universe(Base):
    __tablename__ = 'universe'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    size = Column(Float, nullable=False)
    composition = Column(Text)

    galaxy = relationship('Galaxy', back_populates='universe')

import uuid

from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from . import Base


class Constellation(Base):
    __tablename__ = 'constellation'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    galaxy_id = Column(UUID(as_uuid=True), ForeignKey('galaxy.id'))
    name = Column(String(50), nullable=False)
    shape = Column(String(50))
    abbreviation = Column(String(50))
    history = Column(Text)

    galaxy = relationship('Galaxy', back_populates='constellation')
    star_constellation = relationship('StarConstellation', back_populates='constellation')

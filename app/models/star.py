import uuid

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Star(Base):
    __tablename__ = 'star'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    galaxy_id = Column(UUID(as_uuid=True), ForeignKey('galaxy.id'))
    spectral_type = Column(String(50), nullable=False)
    luminosity = Column(Float, nullable=False)
    distance_from_earth = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)

    galaxy = relationship('Galaxy', back_populates='star')
    planet = relationship('Planet', back_populates='star')
    star_constellation = relationship('StarConstellation', back_populates='star')

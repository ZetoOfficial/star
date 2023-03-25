from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from . import Base


class StarConstellation(Base):
    __tablename__ = 'star_constellation'

    star_id = Column(UUID(as_uuid=True), ForeignKey('star.id'), nullable=False, primary_key=True)
    constellation_id = Column(UUID(as_uuid=True), ForeignKey('constellation.id'), nullable=False, primary_key=True)

    star = relationship('StarConstellation', back_populates='star_constellation')
    constellation = relationship('StarConstellation', back_populates='star_constellation')

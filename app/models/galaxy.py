import uuid

from sqlalchemy import Column, Float, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Galaxy(Base):
    __tablename__ = 'galaxy'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    universe_id = Column(UUID(as_uuid=True), ForeignKey('universe.id'))
    size = Column(Float, nullable=False)
    shape = Column(String(50))
    composition = Column(Text)
    distance_from_earth = Column(Float)

    universe = relationship('Universe', back_populates='galaxy')
    star = relationship('Star', back_populates='galaxy')
    constellation = relationship('Constellation', back_populates='galaxy')

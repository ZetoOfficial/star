import uuid

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Planet(Base):
    __tablename__ = "planet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    mass = Column(Float, nullable=False)
    diameter = Column(Float, nullable=False)
    distance_from_star = Column(Float, nullable=False)
    surface_temperature = Column(Float)
    star_id = Column(UUID(as_uuid=True), ForeignKey("star.id", ondelete="CASCADE"))

    star = relationship("Star", back_populates="planet")

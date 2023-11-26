from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class StarConstellation(Base):
    __tablename__ = "star_constellation"

    star_id = Column(
        UUID(as_uuid=True),
        ForeignKey("star.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    constellation_id = Column(
        UUID(as_uuid=True),
        ForeignKey("constellation.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )

    star = relationship("Star", back_populates="constellations")
    constellation = relationship("Constellation", back_populates="stars")

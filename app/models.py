from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base


class Position(Base):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True, nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    device_ref_id = Column(Integer, ForeignKey("device.id",ondelete="CASCADE"), nullable=False)
    
class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True, nullable=False)
    device_id = Column(Integer, nullable=False)


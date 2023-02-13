from pydantic import BaseModel, Field
from typing import List


class Position(BaseModel):
    device_id: int
    latitude: float
    longitude: float

    class Config:
        orm_mode = True

class PositionResp(BaseModel):
    device_ref_id: int 
    latitude: float
    longitude: float

    class Config:
        orm_mode = True

class PositionResp2(BaseModel):
    # id: int
    device_ref_id: int 
    latitude: float
    longitude: float

    class Config:
        orm_mode = True

class PositionList(Position):
    items: List[Position]

    class Config:
        orm_mode = True

class Device(BaseModel):
    device_id: int

    class Config:
        orm_mode = True

class DeviceList(Device):
    items: List[Device]

    class Config:
        orm_mode = True

class DeviceOut(Device):
    id: int
    device_id: int

    class Config:
        orm_mode = True
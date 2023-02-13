from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from ..database import get_db, save_item
from sqlalchemy.orm import Session
from .. import schemas, models

router = APIRouter(
    prefix = '/position',
    tags = ['Posições do dispositivo']
)

@router.get("/{id}", response_model=List[schemas.Position])
def  get_post(id:int, db: Session = Depends(get_db)):
    position = db.query(models.Device.device_id.label('device_id'), models.Position.latitude.label('latitude'), models.Position.longitude.label('longitude')).outerjoin(models.Device, models.Device.id == models.Position.device_ref_id).filter(models.Device.device_id == id).all()
    if not position:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existem coordenadas atreladas ao id {id}.")

    return position


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=List[schemas.Position])
def save_position_list(items: List[schemas.Position], db: Session = Depends(get_db)):
    response = []
    for item in items:
        device_id_exists = db.query(models.Device).filter(models.Device.device_id == item.device_id).first()
        if device_id_exists == None:
            new_device = models.Device(device_id = item.device_id)
            save_item(new_device,db)
            device_ref_id = new_device.id
        else:
            device_ref_id = device_id_exists.id

        response.append(item.copy())
        
        del item.device_id
        new_position = models.Position(**item.dict(), device_ref_id = device_ref_id)
        save_item(new_position,db)

    return response
from fastapi import APIRouter, status, Depends, HTTPException
from typing import Dict, List
from ..database import get_db, save_item
from sqlalchemy.orm import Session
from .. import schemas, models

router = APIRouter(
    prefix = '/device',
    tags = ['Cadastro de dispositivo']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def save_device_list(items: List[schemas.Device], db: Session = Depends(get_db)):
    response = []
    for item in items:
        device_id_exists = db.query(models.Device).filter(models.Device.device_id == item.device_id).first()
        
        if device_id_exists == None:
            new_device = models.Device(device_id = item.device_id)
            save_item(new_device,db)

            new_device = models.Device(**item.dict())
            response.append(new_device)

    return response
from fastapi import FastAPI
from .routers import device_position, device

app = FastAPI()

app.include_router(device_position.router)
app.include_router(device.router)


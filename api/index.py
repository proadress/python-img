from fastapi import FastAPI
from .xray import xray
from .car import car
app = FastAPI()
app.include_router(xray, prefix="/api/xray", tags=["xray"])
app.include_router(car, prefix="/api/car", tags=["car"])

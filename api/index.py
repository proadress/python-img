from fastapi import FastAPI
from .xray import xray
from .car import car
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(xray, prefix="/api/xray", tags=["xray"])
app.include_router(car, prefix="/api/car", tags=["car"])

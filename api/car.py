from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from api.carImg import start_matching_license

car = APIRouter()


class Image(BaseModel):
    filename: str
    content_type: str
    contents: bytes


@car.post("/image/res")
async def a(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img_bytes = start_matching_license(request_object_content)
    return img_bytes

from typing import List
from fastapi import APIRouter, File, Response, UploadFile
from pydantic import BaseModel
from .xrayRedDot import imgPreset, imgVertices

xray = APIRouter()


class Image(BaseModel):
    filename: str
    content_type: str
    contents: bytes


@xray.post("/image/res")
async def a(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img_bytes = imgPreset(request_object_content)
    # 返回图像的 Response 对象，设置正确的 Content-Type
    return Response(content=img_bytes, media_type="image/jpeg")


@xray.post("/image/mul")
async def upload(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        request_object_content: Image = await file.read()
        img_bytes = imgVertices(request_object_content)
        images.append(img_bytes)
    print(images)
    return str(images)

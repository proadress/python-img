from typing import List
from fastapi import FastAPI, File, Response, UploadFile
from pydantic import BaseModel

app = FastAPI()

import os

extension = ".jpg"
patternsPath = "api/solid_patterns/"


@app.get("/api/test")
def test_():
    return "test"


# @app.post("/api/car/image/res")
# async def a(file: UploadFile = File(...)):
#     request_object_content = await file.read()
#     img_bytes = start_matching_license(request_object_content)
#     return img_bytes


# class Image(BaseModel):
#     filename: str
#     content_type: str
#     contents: bytes


# @app.post("/api/xray/image/res")
# async def a(file: UploadFile = File(...)):
#     request_object_content = await file.read()
#     img_bytes = imgPreset(request_object_content)
#     # 返回图像的 Response 对象，设置正确的 Content-Type
#     return Response(content=img_bytes, media_type="image/jpeg")


# @app.post("/api/xray/image/mul")
# async def upload(files: List[UploadFile] = File(...)):
#     images = []
#     for file in files:
#         request_object_content: Image = await file.read()
#         img_bytes = imgVertices(request_object_content)
#         images.append(img_bytes)
#     print(images)
#     return str(images)



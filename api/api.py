from typing import List
from fastapi import APIRouter, File, Response, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from .reddot import imgPreset, imgVertices

api = APIRouter(prefix="/api", tags=["api"])


class Image(BaseModel):
    filename: str
    content_type: str
    contents: bytes


@api.post("/image/res")
async def a(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img_bytes = imgPreset(request_object_content)
    # 返回图像的 Response 对象，设置正确的 Content-Type
    return Response(content=img_bytes, media_type="image/jpeg")


@api.post("/image/mul")
async def upload(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        request_object_content:Image = await file.read()
        img_bytes = imgVertices(request_object_content)
        images.append(img_bytes)
    print(images)
    return str(images)


# @api.get("/image/original")
# async def linelink():
#     img = cv2.imread("api/image2.jpg")
#     img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

#     ret, img_encoded = cv2.imencode(".jpg", img)
#     img_bytes = img_encoded.tobytes()
#     return Response(content=img_bytes, media_type="image/jpeg")


# @api.post("/upload")
# def upload(file: UploadFile = File(...)):
#     try:
#         contents = file.file.read()
#         with open(file.filename, "wb") as f:
#             f.write(contents)
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         file.file.close()

#     return {"message": f"Successfully uploaded {file.filename}"}

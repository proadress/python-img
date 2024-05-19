from typing import List
from fastapi import FastAPI, File, Response, UploadFile
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)
if not MONGO_URI:
    MONGO_URI = "mongodb+srv://yc359032:jYW7xwHcvGiQDqCp@cluster0.8lnefaq.mongodb.net/?retryWrites=true&w=majority"


class MongoServer:
    def __init__(self, dbname, dbcoll):
        client = MongoClient(MONGO_URI, server_api=ServerApi("1"))
        try:
            client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            client = MongoClient(MONGO_URI)
            db = client[dbname]
            self.coll = db[dbcoll]
        except Exception as e:
            print(e)


db = MongoServer(
    dbname="iot",
    dbcoll="sensordata",
)




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return RedirectResponse("/docs")

@app.get("/data")
async def home():
    return "dhjij"


class sensorData(BaseModel):
    ID:int
    Distance:float

@app.post("/sensorData")
async def home(data :sensorData):
    print(data.ID,data.Distance)
    if(db.coll.find({"_id":data.ID})):
        db.coll.replace_one({"_id": data.ID}, {"_id": data.ID, "dis": data.Distance})
    else:
        db.coll.insert_one({"_id":data.ID,"dis":data.Distance})
    return "success"

@app.get("/db/sensorData")
async def home(id:int):
    return db.coll.find_one({"_id":id})

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



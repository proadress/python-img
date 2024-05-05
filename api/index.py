from typing import List
from fastapi import FastAPI, File, Response, UploadFile
from pydantic import BaseModel

app = FastAPI()

import os
import cv2
import numpy as np

extension = ".jpg"
patternsPath = "api/solid_patterns/"


@app.get("/api/test")
def test_():
    return "test"


@app.post("/api/car/image/res")
async def a(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img_bytes = start_matching_license(request_object_content)
    return img_bytes


class Image(BaseModel):
    filename: str
    content_type: str
    contents: bytes


@app.post("/api/xray/image/res")
async def a(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img_bytes = imgPreset(request_object_content)
    # 返回图像的 Response 对象，设置正确的 Content-Type
    return Response(content=img_bytes, media_type="image/jpeg")


@app.post("/api/xray/image/mul")
async def upload(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        request_object_content: Image = await file.read()
        img_bytes = imgVertices(request_object_content)
        images.append(img_bytes)
    print(images)
    return str(images)


def start_matching_license(img_bytes):
    img_array = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
    rawImage = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    contours, hierarchy = cv2.findContours(
        cv2.Canny(
            cv2.GaussianBlur(
                cv2.bilateralFilter(
                    cv2.cvtColor(rawImage, cv2.COLOR_BGR2GRAY), 11, 17, 17
                ),
                (5, 5),
                0,
            ),
            170,
            200,
        ),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE,
    )  # 轉為灰階，去除背景雜訊，高斯模糊，取得邊緣，取得輪廓
    rectangleContours = []  # 為四邊形的集合
    for contour in sorted(contours, key=cv2.contourArea, reverse=True)[
        :30
    ]:  # 只取前三十名輪廓
        if (
            len(cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True))
            == 4
        ):  # 取得輪廓周長*0.02(越小，得到的多邊形角點越多)後，得到多邊形角點，為四邊形者
            rectangleContours.append(contour)
    x, y, w, h = cv2.boundingRect(
        rectangleContours[0]
    )  # 只取第一名，用一個最小的四邊形，把找到的輪廓包起來。
    ret, plateImage = cv2.threshold(
        cv2.cvtColor(
            cv2.GaussianBlur(rawImage[y : y + h, x : x + w], (3, 3), 0),
            cv2.COLOR_RGB2GRAY,
        ),
        0,
        255,
        cv2.THRESH_OTSU,
    )  # 找到車牌後，由原來的圖截取出來，再將其高斯模糊以及取得灰階，再獲得Binary圖

    # 取出車牌文字 Getting License Plate Number
    contours, hierarchy = cv2.findContours(
        plateImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )  # 取得車牌文字輪廓
    letters = []
    for contour in contours:  # 遍歷取得的輪廓
        rect = cv2.boundingRect(contour)
        if (rect[3] > (rect[2] * 1.5)) and (
            rect[3] < (rect[2] * 3.5) and (rect[2] > 10)
        ):  # 過濾雜輪廓
            letters.append(cv2.boundingRect(contour))  # 存入過濾過的輪廓
    letter_images = []
    for letter in sorted(
        letters, key=lambda s: s[0], reverse=False
    ):  # 重新安排號碼順序遍歷
        letter_images.append(
            plateImage[
                letter[1] : letter[1] + letter[3], letter[0] : letter[0] + letter[2]
            ]
        )  # 將過濾過的輪廓使用原圖裁切
    results = []
    for index, letter_image in enumerate(letter_images):
        best_score = []
        patterns = os.listdir(patternsPath)
        for filename in patterns:  # 讀取資料夾下所有的圖片
            ret, pattern_img = cv2.threshold(
                cv2.cvtColor(
                    cv2.imdecode(
                        np.fromfile(patternsPath + filename, dtype=np.uint8), 1
                    ),
                    cv2.COLOR_RGB2GRAY,
                ),
                0,
                255,
                cv2.THRESH_OTSU,
            )  # 將範本進行格式轉換，再獲得Binary圖
            pattern_img = cv2.resize(
                pattern_img, (letter_image.shape[1], letter_image.shape[0])
            )  # 將範本resize至與圖像一樣大小
            best_score.append(
                cv2.matchTemplate(letter_image, pattern_img, cv2.TM_CCOEFF)[0][0]
            )  # 範本匹配，返回匹配得分
        i = best_score.index(max(best_score))  # 取得最高分的index
        results.append(patterns[i])
    ans = "".join(results).replace(extension, "")  # Printing Rusults To Console
    print(ans)
    return ans


def imgPreset(img_bytes):
    img_array = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 110, 0])
    upper = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    blackResult = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(blackResult, 150, 200)
    contours, hierarchy = cv2.findContours(
        canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    tempList = []
    for cnt in contours:
        tempList.append(cv2.contourArea(cnt))
        cv2.drawContours(img, cnt, -1, (255, 255, 255), 2)
        area = cv2.contourArea(cnt)
        # print(cv2.arcLength(cnt, True))
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.05, True)
        # print(vertices)
        vertices = [list(v[0]) for v in vertices]
        vertices = sorted(vertices, key=lambda x: x[1])
        print(vertices)

        cv2.rectangle(
            img,
            (vertices[0][0] - 5, vertices[0][1] - 5),
            (vertices[0][0] + 5, vertices[0][1] + 5),
            (0, 105, 0),
            2,
        )
        cv2.putText(
            img,
            str(vertices[0]),
            (vertices[0][0], vertices[0][1] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
        )
        # 将图像转换为 JPEG 格式的二进制数据
    cv2.putText(
        img,
        str(random.randint(1, 10)),
        (0, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )
    ret, img_encoded = cv2.imencode(".jpg", img)
    img_bytes = img_encoded.tobytes()
    return img_bytes


def imgVertices(img_bytes):
    img_array = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 110, 0])
    upper = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    blackResult = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(blackResult, 150, 200)
    contours, hierarchy = cv2.findContours(
        canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    tempList = []
    for cnt in contours:
        # tempList.append(cv2.contourArea(cnt))
        cv2.drawContours(img, cnt, -1, (255, 255, 255), 2)
        area = cv2.contourArea(cnt)
        # print(cv2.arcLength(cnt, True))
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.1, True)
        # print(vertices)
        vertices = [list(v[0]) for v in vertices]
        vertices = sorted(vertices, key=lambda x: x[1])
        tempList.append(vertices[0])
    return tempList

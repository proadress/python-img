import cv2
import numpy as np
import random


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

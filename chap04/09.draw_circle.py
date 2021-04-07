"""
cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]]) -> img
center 를 중심으로 radius 반지름의 원을 그리낟
- img: 원을 그릴 대상 행렬(영상)
- center: 원의 중심 좌표
- radius: 원의 반지름
- color: 선의 색상
- thickness: 선의 두께
- lineType: 선의 형태, cv2.line() 함수의 인수와 동일
- shift: 좌표에 대한 비트 시프트 연산
"""

import numpy as np
import cv2 as cv

orange, blue, cyan = (0, 165, 255), (255, 0, 0), (255, 255, 0)
white, black = (255, 255, 255), (0, 0, 0)
image = np.full((300, 500, 3), white, np.uint8)  # 컬러 영상 생성 및 초기화

center = (image.shape[1] // 2, image.shape[0] // 2)  # 영상 중심 좌표 - 역순 구성
pt1, pt2 = (300, 50), (100, 220)
shade = (pt2[0] + 2, pt2[1] + 2)  # 그림자 좌표

cv.circle(image, center, 100, blue)  # 원 그리기
cv.circle(image, pt1, 50, orange, 2)
cv.circle(image, pt2, 70, cyan, -1)  # 원 내부 채움

font = cv.FONT_HERSHEY_COMPLEX
cv.putText(image, "Center Blue", center, font, 1.0, blue)
cv.putText(image, "pt1 Orange", pt1, font, 0.8, orange)
cv.putText(image, "pt2 Cyan", shade, font, 1.2, black, 2)  # 그림자 효과
cv.putText(image, "pt2 Cyan", pt2, font, 1.2, cyan, 1)

cv.imshow("Draw Circles", image)
cv.waitKey(0)
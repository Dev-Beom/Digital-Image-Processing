"""
cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
- img: 문자열을 작성할 대상 행렬(영상)
- text: 작성할 문자열
- org: 문자열의 시작 좌표, 문자열에서 가장 왼쪽 하단을 의미
- fontFace: 문자열의 폰트
- fontScale: 글자 크기 확대 비율
- color: 글자의 색상
- thickness: 글자의 굵기
- lineType: 글자 선의 형태
- bottomLeftOrigin: 영상의 원점 좌표 설정(True - 좌하단 왼족, False - 좌상단)
"""

import numpy as np
import cv2 as cv

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 200), (50, 260)  # 문자열 위치 좌표

image = np.zeros((300, 500, 3), np.uint8)
image.fill(255)

cv.putText(image, "SIMPLEX", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, brown)
cv.putText(image, "DUPLEX", (50, 130), cv.FONT_HERSHEY_DUPLEX, 3, olive)
cv.putText(image, "TRIPLEX", pt1, cv.FONT_HERSHEY_TRIPLEX, 2, violet)
fontFace = cv.FONT_HERSHEY_PLAIN | cv.FONT_ITALIC  # 글자체 상수
cv.putText(image, "ITALIC", pt2, fontFace, 4, violet)

cv.imshow("Put Text", image)
cv.waitKey(0)  # 키 이벤트 대기

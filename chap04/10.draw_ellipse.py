"""
cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]) -> img
center 를 중심으로 axes 크기의 타원을 그린다.
- img: 그릴 대상 정렬(영상)
- center: 원의 중심 좌표
- axes: 타원의 절반 크기(x축 반지름, y축 반지름)
- angle: 타원의 각도(3시 방향이 0도, 시계방향 회전)
- startAngle: 호의 시작 각도
- endAngle: 호의 종료 ㄱ가도
- color: 선의 색상
- thickness: 선의 두께
- lineType: 선의 형태
- shift: 좌표에 대한 비트 시프트
"""

import numpy as np
import cv2 as cv

orange, blue, white = (0, 165, 255), (255, 0, 0), (255, 255, 255)  # 색상 지정
image = np.full((300, 700, 3), white, np.uint8)  # 3채널 행렬 생성 및 초기화

pt1, pt2 = (180, 150), (550, 150)  # 타원 중심점
size = (120, 60)  # 타원 크기 - 반지름 값임

cv.circle(image, pt1, 1, 0, 2)  # 타원의 중심점(2화소 원) 표시
cv.circle(image, pt2, 1, 0, 2)

cv.ellipse(image, pt1, size, 0, 0, 360, blue, 1)  # 타원 그리기
cv.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
cv.ellipse(image, pt1, size, 0, 30, 270, orange, 4)  # 호 그리기
cv.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

cv.imshow("문자열", image)
cv.waitKey()  # 키입력 대기

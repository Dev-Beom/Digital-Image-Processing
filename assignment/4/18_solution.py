import numpy as np
import cv2

title = "image"
red, blue = (0, 0, 255), (255, 0, 0)
white = (255, 255, 255)
image = np.full((200, 300, 3), white, np.uint8)  # 컬러 영상 생성 및 초기화

center = (image.shape[1] // 2, image.shape[0] // 2)  # 영상 중심 좌표 - 역순 구성
right = (image.shape[1] // 2 + 25, image.shape[0] // 2)
left = (image.shape[1] // 2 - 25, image.shape[0] // 2)

image.fill(255)

MIN = (25, 25)
MAX = (50, 50)

cv2.ellipse(image, center, MAX, 0, 180, 360,  red, -1)  # 위 빨간색
cv2.ellipse(image, center, MAX, 0, 0, 180, blue, -1)  # 아래 파란색
cv2.ellipse(image, right, MIN, 0, 180, 360, blue, -1)  # 미니 위 파란색
cv2.ellipse(image, left, MIN, 0, 0, 180, red, -1)  # 미니 아래 빨간색

cv2.imshow(title, image)
cv2.waitKey(0)

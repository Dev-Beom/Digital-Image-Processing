import cv2
import numpy as np

hsvmap = np.zeros((180, 255, 3), np.uint8)
h, s = np.indices(hsvmap.shape[:2])

hsvmap[:, :, 0] = h
hsvmap[:, :, 1] = s
hsvmap[:, :, 2] = 255

hsvmap = cv2.cvtColor(hsvmap, cv2.COLOR_HSV2BGR)

img = cv2.imread('mk.jpg')
originalImg = cv2.imread('mk.jpg')
cv2.namedWindow('dst', 0)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 255], [0, 180, 0, 255])

hist = np.clip(hist * 0.005 * 50, 0, 1)
hist = hsvmap * hist[:, :, np.newaxis] / 255

cv2.imshow('dst', hist)
cv2.imshow('image', originalImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

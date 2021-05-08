import cv2 as cv

alpha_slider_max = 100
beta_slider_max = 100
theta_slider_max = 100
title_window = 'Blend'


def onChanged(val):
    alpha = cv.getTrackbarPos('1', title_window) * 0.01
    beta = cv.getTrackbarPos('2', title_window) * 0.01
    theta = cv.getTrackbarPos('3', title_window) * 0.01

    dst1 = cv.addWeighted(src1, alpha, src2, beta, 0)
    dst = cv.addWeighted(dst1, 1, src3, theta, 0)

    cv.imshow(title_window, dst)


src1 = cv.imread("./image/r1.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("./image/r2.jpg", cv.IMREAD_COLOR)
src3 = cv.imread("./image/r3.jpg", cv.IMREAD_COLOR)

cv.namedWindow(title_window)

cv.createTrackbar('1', title_window, 0, alpha_slider_max, onChanged)
cv.createTrackbar('2', title_window, 0, beta_slider_max, onChanged)
cv.createTrackbar('3', title_window, 0, beta_slider_max, onChanged)

onChanged(0)

cv.waitKey()

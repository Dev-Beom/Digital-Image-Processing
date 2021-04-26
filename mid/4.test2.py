import cv2 as cv

alpha_slider_max = 100
beta_slider_max = 100
theta_slider_max = 100
title_window = 'Blend'


def onChange(val):
    alpha = cv.getTrackbarPos('1', title_window)*0.01
    beta = cv.getTrackbarPos('2', title_window)*0.01
    theta = cv.getTrackbarPos('3', title_window)*0.01

    dst1 = cv.addWeighted(src1, alpha, src2, beta, 0)
    dst = cv.addWeighted(dst1, 1, src3, theta, 0)

    cv.imshow(title_window, dst)


src1 = cv.imread("img-1.jpg", cv.IMREAD_COLOR)
src2 = cv.imread("img-2.jpg", cv.IMREAD_COLOR)
src3 = cv.imread("img-3.jpg", cv.IMREAD_COLOR)

cv.namedWindow(title_window)

cv.createTrackbar('1', title_window , 0, alpha_slider_max, onChange)
cv.createTrackbar('2', title_window , 0, beta_slider_max, onChange)
cv.createTrackbar('3', title_window , 0, beta_slider_max, onChange)


# Show some stuff
onChange(0)

# Wait until user press some key
cv.waitKey()
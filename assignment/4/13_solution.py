import cv2

windowTitle = "Color to Gray"
image = cv2.imread("images/image_color.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 에러")
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 100)  # JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 0]  # PNG 압축 레벨 설정

# 행렬을 영상파일로 저장
cv2.imwrite("images/test.jpg", image, params_jpg)
cv2.imwrite("images/test.png", image, params_png)
cv2.imshow(windowTitle, image)
cv2.waitKey(0)


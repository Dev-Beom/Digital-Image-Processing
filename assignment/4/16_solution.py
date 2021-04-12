import cv2

title = "Camera"
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise Exception("카메라 연결 안됨")

x = 200
y = 100
w = 100
h = 200
while True:
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(30) >= 0:
        break
    roi = frame[y:y + h, x:x + w]
    # newFrame = roi.copy()
    green = frame[y:y + h, x:x + w][:, :, :]
    cv2.add(50, green, green)

    cv2.rectangle(roi, (0, 0), (w - 1, h - 1), (0, 0, 255), 3)
    cv2.imshow(title, frame)
capture.release()

import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps = 15  # 초당 프레임 수
delay = round(1000 / fps)  # 프레임 간 지연 시간
size = (640, 580)  # 동영상파일 해상도
fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 압축 코덱 설정

capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

# 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("images/flip_test.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(delay) >= 0: break
    frameFlip = cv2.flip(frame, 1)
    writer.write(frame)
    cv2.imshow("View Frame form Camera", frame)
    cv2.imshow("View Flip Frame form Cemera", frameFlip)

writer.release()
capture.release()

import cv2

drawing = False
point1 = ()
point2 = ()


def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
        else:
            drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing is True:
            drawing = False
            point2 = (x, y)


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)

while True:
    _, frame = cap.read()

    if point1 and point2:
        cv2.rectangle(frame, point1, point2, (0, 0, 255))
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

import numpy as np, cv2

pts1 = np.array([(100, 100, 1), (400, 100, 1), (400, 250, 1), (100, 250, 1)], np.float32)

theta = 45 * np.pi / 180
m = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta), np.cos(theta), 0],
              [0, 0, 1]], np.float32)

delta = (pts1[2] - pts1[0]) // 2
center = pts1[0] + delta

a = np.array([center, center, center, center])
t1 = pts1 - a
t2 = a

m2 = cv2.gemm(t1, m, 1, None, 1, flags=cv2.GEMM_2_T)
pts2 = m2 + a

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("pts1[%d] = %s, pts2[%d]= %s" % (i, pt1, i, pt2))

image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1[:, :2])], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2[:, :2])], True, (255, 0, 0), 3)
cv2.imshow("image", image)
cv2.waitKey(0)
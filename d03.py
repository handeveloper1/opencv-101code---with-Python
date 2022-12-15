import cv2
import numpy as np

img = cv2.imread("test.jpg")
kernel = np.ones((5,5), np.uint8)

imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imGray, (7,7), 0)


imgCanny = cv2.Canny(img, 150, 200)


cv2.imshow("Gray", imGray)

cv2.imshow("imgBlur", imgBlur)

cv2.imshow("imgCanny", imgCanny)

cv2.waitKey(0)
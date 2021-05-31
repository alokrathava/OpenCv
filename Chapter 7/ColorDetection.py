import cv2
import numpy as np


def empty(a):
    pass


path = 'assets/lambo.png'
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Saturation Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Saturation Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Value Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Value Max", "Trackbars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Saturation Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Saturation Max", "Trackbars")
    val_min = cv2.getTrackbarPos("Value Min", "Trackbars")
    val_max = cv2.getTrackbarPos("Value Max", "Trackbars")

    print(h_min, h_max, s_min, s_max, val_min, val_max)
    lower = np.array([h_min, s_min, val_min])
    higher = np.array([h_max, s_max, val_max])
    mask = cv2.inRange(imgHSV, lower, higher)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(1)

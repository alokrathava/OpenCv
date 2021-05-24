import cv2
import numpy as np

img = cv2.imread("assets/cards.jpg")
kernel = np.ones((5, 5), np.uint8)  # uint8 means unassigned int of 8 bits 0-255.

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Gray Image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # Blur Image
imgCanny = cv2.Canny(imgGray, 100, 100)  # Edge Detection using Canny
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # Dialation of canny image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)  # Image Erossion

cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilated Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

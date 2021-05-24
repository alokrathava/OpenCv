import cv2
import numpy as np

# Image Resizing
img = cv2.imread("assets/lambo.png")
print(img.shape)  # (462 width,623 height, 3 channels BGR)

imgResize = cv2.resize(img, (300, 200))  # (width, height)
print(imgResize.shape)

# Image Cropping
imgCropped = img[0:200, 200:500]  # (height,width)
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)

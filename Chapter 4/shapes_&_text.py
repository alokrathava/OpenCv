import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
# Color
# img[200:300, 100:150] = 255, 000, 000  # BLUE
# img[:] = 000, 255, 000  # GREEN
# img[:] = 000, 000, 255  # RED

# Shapes
# Line
cv2.line(img, (100, 100), (400, 400), (0, 183, 00), 3)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 183, 00), 3)
# Rectangle
cv2.rectangle(img, (0, 0), (300, 300), (0, 183, 0), 3)
# Circle
cv2.circle(img, (290, 290), 50, (0, 183, 0), 3)
# Text
cv2.putText(img, "Cartoon", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 183), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)

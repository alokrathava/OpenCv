import cv2

# Read Images
img = cv2.imread("assets/lena.png")
cv2.imshow("Read Images",img)
cv2.waitKey(0)

# Read Video
video = cv2.VideoCapture("assets/test.mp4")
while True:
    success, img = video.read()
    cv2.imshow("Read Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Read From Camera
cap = cv2.VideoCapture(0)
cap.set(3, 360) #Width
cap.set(4, 480) #Height
cap.set(10, 100) #Brightness

while True:
    success, img = cap.read()
    cv2.imshow("Read Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

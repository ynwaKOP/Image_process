import cv2
import time

video = cv2.VideoCapture(0)

count = 0

while True:

    count = count+1
    check, frame = video.read()

    print(check)
    print(frame)

    #cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #time.sleep(3)
    cv2.imshow('video capture', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(count)
video.release()
cv2.destroyAllWindows()
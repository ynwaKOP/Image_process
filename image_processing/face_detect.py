import cv2
import os

os.chdir('Files')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('myphoto.jpg')

faces = face_cascade.detectMultiScale(img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 4)

re_sz = cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))

cv2.imshow('show window',re_sz)
cv2.waitKey(0)
cv2.destroyAllWindows()

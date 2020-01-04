import cv2
import os, glob

img_size = (100,100)

os.chdir("sample-images")

for image in glob.glob("*.jpg"):
    img = cv2.imread(image,1)
    new_img = cv2.resize(img,img_size)
    cv2.imwrite('resized_'+image,new_img)




import cv2

img = cv2.imread('galaxy.jpg',0)

"""
print(img)
print(type(img))

print(img.shape)
print(img.ndim)
"""

resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))


#cv2.imshow('show window',resized_img)
#cv2.waitKey(0)
cv2.imwrite('galaxy_bnw.jpg',resized_img)

#cv2.destroyAllWindows()
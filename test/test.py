import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('img1.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
r = 500.0/hsv.shape[1]
dim = (500, int(hsv.shape[0]*r))
resized = cv2.resize(hsv, dim, interpolation=cv2.INTER_AREA)
img_resize = cv2.resize(img,dim, interpolation=cv2.INTER_AREA)


eximg = cv2.imread('ex1.jpg',0)
w,h = eximg.shape

res = cv2.matchTemplate(resized,eximg,cv2.TM_CCORR_NORMED)
thresh = 0.811
loc =np.where(res>=thresh)
print(loc)
for pt in zip(*loc[::-1]):
    print(pt)
    cv2.rectangle(img_resize,pt,(pt[0]+w,pt[1]+h),(0,0,0),1)
cv2.imshow('image',img_resize)
cv2.waitKey(0)
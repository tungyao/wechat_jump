import cv2
import numpy as np
import matplotlib.pyplot as plt
def go(path):
    img = cv2.imread(path)
    r = 500.0/img.shape[1]
    dim = (500, int(img.shape[0]*r))
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

    corner = cv2.goodFeaturesToTrack(gray,200,0.01,10)
    corner = np.int16(corner)
    for c in corner:
        x,y  = c.ravel()
        cv2.circle(gray,(x,y),3,255,1)
    cv2.imshow('image',gray)
    cv2.waitKey()
def go2():
    img1 = cv2.imread('img0.jpg',1)
    img2 = cv2.imread('img4.jpg',1)
    orb = cv2.ORB_create()
    kp1,des1 = orb.detectAndCompute(img1,None)
    kp2,des2 = orb.detectAndCompute(img1,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches =bf.match(des1,des2)
    matches = sorted(matches,key=lambda x:x.distance)
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:8],None,flags=2)
    plt.imshow(img3)
    plt.show()
if __name__=="__main__":
    go2()
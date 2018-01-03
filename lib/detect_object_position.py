import cv2
import numpy as np
def get_obj_position():
    fn = "../test/img5.jpg"
    src = cv2.imread(fn, 0)
    r = 500.0 / src.shape[1]
    dim = (500, int(src.shape[0] * r))
    img = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)
    # img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(src,(3,3),0)
    cimg = src.copy() # numpy function

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 4, np.array([]), 100, 40, 0, 35)
    point = None

    canny = cv2.Canny(img,50,100,apertureSize = 3)
    if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
        a, b, c = circles.shape
        for i in range(b):
            a = circles[0][i][0]
            b = circles[0][i][1]
            cv2.circle(canny, (a, b), circles[0][i][2], (255, 255, 255), 2, cv2.LINE_AA)
            cv2.circle(canny, (a ,int(b)+70), 3, (255, 255, 255), 1, cv2.LINE_AA)  # draw center of circle
            point =[circles[0][i][0], circles[0][i][1]-100]
    hof = cv2.HoughLines(canny,1,np.pi/180,90)
    line = hof[:,0,:]
    for r,theta in line[:]:
        print(r,theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * r
        y0 = b * r
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
        cv2.line(canny, (x1, y1), (x2, y2), (255, 255, 255), 3)
    cv2.imshow("a", canny)
    # cv2.imshow("b", img)
    print("INFO point0 is %s"%(point))
    cv2.waitKey(0)
    return point
if __name__=="__main__":
    get_obj_position()
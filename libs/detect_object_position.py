import cv2,time
import numpy as np
from adb_operations import adb
from calculation_pressure_time import calcula

class detect():
    point = None
    IMG =None
    def read(self):
        press = adb()
        press.cut_screen()

        fn = "E:\hub\yum\data\img1.jpg"
        src = cv2.imread(fn)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        r = 500.0 / src.shape[1]
        dim = (500, int(src.shape[0] * r))
        self.IMG = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)
    def update(self):
        fn = "E:\hub\yum\data\img1.jpg"
        src = cv2.imread(fn)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        r = 500.0 / src.shape[1]
        dim = (500, int(src.shape[0] * r))
        imgs = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)
        self.IMG=imgs
    def cannys(self):
        # img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # img = cv2.GaussianBlur(src,(3,3),0)
        imgs = cv2.GaussianBlur(self.IMG, (3, 3), 0)

        circles = cv2.HoughCircles(imgs, cv2.HOUGH_GRADIENT, 1, 4, np.array([]), 100, 40, 0, 35)
        canny = cv2.Canny(imgs,50,100,apertureSize = 3)
        if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
            a, b, c = circles.shape
            for i in range(b):
                a = circles[0][i][0]
                b = circles[0][i][1]
                # cv2.circle(canny, (a, b), circles[0][i][2], (255, 255, 255), 2, cv2.LINE_AA)
                cv2.circle(self.IMG, (a ,int(b)+70), 3, (255, 255, 255), 3, cv2.LINE_AA)  # draw center of circle
                self.point =[circles[0][i][0], circles[0][i][1]+70]
        print("INFO point0 is %s"%(self.point))
        # cv2.imshow("a", canny)
        # cv2.imshow("b", img)
        # cv2.waitKey(0)
        return canny,self.point
    def get_jump_to_obj_position(self):
        canny = self.cannys()
        ret, binary = cv2.threshold(self.IMG, 127, 255, cv2.THRESH_BINARY)
        _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(img, contours,-1, (0, 0, 255), 3)
        hof = cv2.HoughLines(canny[0], 1, np.pi / 90,100)
        line = hof[:, 0, :]
        diction = None
        for r, theta in line[:]:
            # print(r)
            a = np.cos(theta)
            b = np.sin(theta)
            # print(a)
            x0 = a * r
            y0 = b * r
            x1 = int(x0 + 100 * (-b))
            y1 = int(y0 + 100 * (a))
            x2 = int(x0 - 100 * (-b))
            y2 = int(y0 - 100 * (a))


            cv2.line(self.IMG, (x1, y1), (x2, y2), (0, 0, 255), 3)
            # cv2.line(canny, (x1, y1), (x2, y2), (255, 255, 255), 3)
        # cv2.imshow('a',canny)
        cv2.namedWindow('b')
        cv2.imshow('b',self.IMG)
        cv2.setMouseCallback('b',self.mouse,canny[1])
        cv2.waitKey(0)
    def mouse(self,event,x,y,flags,param):
        press_time = calcula()
        press = adb()
        if event==cv2.EVENT_LBUTTONDOWN:
            print(param,x,y)
            press_time.POINT = param
            press_time.POINTs = [x,y]
            times = press_time.value()
            press.press(times)
            cv2.destroyWindow('b')
            time.sleep(1)
            press.cut_screen()
            self.update()
            self.get_jump_to_obj_position()


if __name__=="__main__":
    a = detect()
    a.read()
    a.get_jump_to_obj_position()

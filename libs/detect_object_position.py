import cv2, time
import numpy as np
import matplotlib.pyplot as plt
from adb_operations import adb
from calculation_pressure_time import calcula


class detect():
    point = None
    point_head = None
    IMG = None
    IMG_D = None
    TEMPLATE_IMG = None
    TEMPLATE_IMG_D = None

    def read(self):
        press = adb()
        press.cut_screen()
        fn = "E:\hub\yum\data\img.jpg"
        src = cv2.imread(fn,0)
        # src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        r = 500.0 / src.shape[1]
        dim = (500, int(src.shape[0] * r))
        self.IMG = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)
        self.IMG_D = src
        template = 'E:\hub\yum\data\\bg3.jpg'
        tsrc = cv2.imread(template,0)
        # tsrc = cv2.cvtColor(tsrc, cv2.COLOR_BGR2GRAY)
        tr = 300.0 / tsrc.shape[1]
        tdim = (300, int(tsrc.shape[0] * tr))
        self.TEMPLATE_IMG = cv2.resize(tsrc, tdim, interpolation=cv2.INTER_AREA)
        self.TEMPLATE_IMG_D = tsrc

    def update(self):
        cv2.destroyWindow('b')
        fn = "E:\hub\yum\data\img.jpg"
        src = cv2.imread(fn)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        r = 500.0 / src.shape[1]
        dim = (500, int(src.shape[0] * r))
        imgs = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)
        self.IMG = imgs

    def cannys(self):
        imgs = cv2.GaussianBlur(self.IMG, (3, 3), 0)

        circles = cv2.HoughCircles(imgs, cv2.HOUGH_GRADIENT, 1, 4, np.array([]), 100, 40, 0, 35)
        canny = cv2.Canny(imgs, 50, 100, apertureSize=3)
        if circles is not None:  # Check if circles have been found and only then iterate over these and add them to the image
            print(circles)
            a,b,c = circles.shape
            for i in range(b):
                a = circles[0][i][0]
                b = circles[0][i][1]
                # cv2.circle(self.IMG, (a, b), circles[0][i][2], (255, 255, 255), 2, cv2.LINE_AA)
                cv2.circle(self.IMG, (a, b), 3, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.circle(self.IMG, (a, int(b) + 70), 3, (255, 255, 255), 3, cv2.LINE_AA)  # draw center of circle
                self.point_head = [a, b]
                self.point = [a, int(b) + 70]
        print("INFO point_head is %s" % (self.point_head))
        print("INFO point is %s" % (self.point))
        # cv2.imshow("a", canny)
        # cv2.imshow("b", img)
        # cv2.waitKey(0)
        return canny, self.point

    def get_jump_to_obj_position(self):
        point = self.find_box()
        press_time = calcula()
        press = adb()
        press_time.POINT = self.point
        press_time.POINTs = point
        times = press_time.value()
        press.press(times)
        # cv2.imshow('b', self.IMG)
        # cv2.waitKey()
        time.sleep(1)
        press.cut_screen()
        self.update()
        self.get_jump_to_obj_position()
    def mouse(self, event, x, y, flags, param):
        press_time = calcula()
        press = adb()
        if event==cv2.EVENT_LBUTTONDOWN:
            print(x,y)
            press_time.POINT = param
            press_time.POINTs = [x,y]
            times = press_time.value()
            press.press(times)
            cv2.destroyWindow('b')
            time.sleep(1)
            press.cut_screen()
            self.update()
            self.get_jump_to_obj_position()
        # if event == cv2.EVENT_MOUSEMOVE:
        #     print('x :', x, " y :", y, 'point_head :', self.point_head, 'point:', self.point)

    def templeta_find(self):
        template = self.TEMPLATE_IMG
        w, h = template.shape[::-1]
        img = self.IMG
        # print(w,h)
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        # for meth in methods:
        # img = img.copy()

        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(min_loc)
        print(max_loc)
        print(min_val)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        print(top_left,bottom_right)
        cv2.rectangle(self.IMG, top_left, bottom_right,(255,255,255), 5)
        cv2.imshow('name',self.IMG)
        cv2.waitKey()
    def find_box(self):
        canny = self.cannys()
        img =canny[0]
        h,w = img.shape
        print("box w:",w,"h:",h)
        IMG = np.array(self.IMG)
        point = self.point_head
        print('point :',point)

        if point[0] < w/2:
            box = IMG[int(point[0]) * 1:int(point[0]) *3, int(point[0])+10:int(point[1])+30]
            print('target box ',box.shape)
            hs,ws =box.shape
            arr =[]
            point_get = []
            for px in range(len(box)):
                sums = np.average(box[px])
                # print(sums)
                if sums < 210 or sums >170:
                    arr.append(px)
            for i in range(len(arr)):
                box[arr[i]] =255
                point_get.append([ws+100,int(h*3/4-arr[i])+10])
            point_true = point_get[int(len(point_get)/2)]
            print(point_true)
            return [point_true[0],point_true[1]]
        elif point[0] >w/2:
            box = IMG[int(point[0]):int(point[1]),int(point[0]/2):int(point[1]/2)]
            print('target box ', box.shape)
            hs, ws = box.shape
            arr = []
            point_get = []
            for px in range(len(box)):
                sums = np.average(box[px])
                if sums < 210 or sums > 170:
                    arr.append(px)
            for i in range(len(arr)):
                box[arr[i]] = 255
                point_get.append([w-point[0]+ws,h-point[1]-hs])
            point_true = point_get[int(len(point_get) / 2)]
            print(point_true)
            return [point_true[0],point_true[1]]
if __name__ == "__main__":
    a = detect()
    a.read()
    a.get_jump_to_obj_position()

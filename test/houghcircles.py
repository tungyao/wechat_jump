#!/usr/bin/python

'''
This example illustrates how to use cv2.HoughCircles() function.

Usage:
    houghcircles.py [<image_name>]
    image argument defaults to ../data/board.jpg
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys

if __name__ == '__main__':
    try:
        fn = sys.argv[1]
    except IndexError:
        fn = "img3.jpg"

    src = cv2.imread(fn, 0)
    r = 500.0 / src.shape[1]
    dim = (500, int(src.shape[0] * r))
    src = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)
    # img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(src,(1,1),0)
    cimg = src.copy() # numpy function

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 4, np.array([]), 100, 40, 0, 35)
    point = None
    canny = cv2.Canny(img,0,100)
    if circles is not None: # Check if circles have been found and only then iterate over these and add them to the image
        a, b, c = circles.shape
        for i in range(b):
            cv2.circle(canny, (circles[0][i][0], circles[0][i][1]), circles[0][i][2], (255, 255, 255), 2, cv2.LINE_AA)
            cv2.circle(canny, (circles[0][i][0], circles[0][i][1]), 2, (255, 255, 255), 1, cv2.LINE_AA)  # draw center of circle
            point =[circles[0][i][0], circles[0][i][1]]
    print(point)
    cv2.imshow("detected circles", canny)
    cv2.waitKey(0)

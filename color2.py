#二值化图像 看全局阈值即可
#二值化函数代码

import cv2 as cv
import numpy as np

# 全局阈值
def threshold_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #把输入图像灰度化
    #直接阈值化是对输入的单通道矩阵逐像素进行阈值化分割。
    ret,binary = cv.threshold(gray,127,255,cv.THRESH_BINARY|cv.THRESH_TRIANGLE)
    print("threshold value %s"%ret)
    cv.namedWindow("binary0",cv.WINDOW_NORMAL)
    cv.imshow("binary0",binary)

# 局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    cv.namedWindow("binary1", cv.WINDOW_NORMAL)
    cv.imshow("binary1", binary)

# 用户自己计算阈值
def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    m = np.reshape(gray,[1,w*h])
    mean = m.sum()/(w*h)
    print("mean:",mean)
    ret,binary = cv.threshold(gray,mean, 255,cv.THRESH_BINARY)
    cv.namedWindow("binary2", cv.WINDOW_NORMAL)
    cv.imshow("binary2", binary)

src = cv.imread('input.png')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)
cv.imshow('input_image', src)
threshold_demo(src)
local_threshold(src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()

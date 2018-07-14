import cv2
import numpy as np

image=cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
cv2.namedWindow('Origin', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Origin', image)
cv2.namedWindow('Filter', cv2.WINDOW_AUTOSIZE)

# Linear filter

## Blur
''' 
    blur the image just by calc the mean of the kernel window
    ksize: the kernel size
    anchor: anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
'''
blur = cv2.blur(image, ksize=(15, 15), anchor=(-1,-1), borderType = cv2.BORDER_DEFAULT)
cv2.imshow('Filter', blur)
cv2.waitKey(0)

## BoxFilter
'''
    if normalize is True, this is the blur() function.
      True:  Kernel = [[1, ..., 1], ..., [1, ..., 1]] / sum(Kernel)
      False: Kernel = [[1, ..., 1], ..., [1, ..., 1]]
'''
boxf = cv2.boxFilter(image, ddepth=cv2.CV_8U, ksize=(3, 3), anchor=(-1,-1), normalize=False, borderType = cv2.BORDER_DEFAULT)
cv2.imshow('Filter', boxf)
cv2.waitKey(0)

## filter2D
'''
    this kernel actually is the blur with ksize=(15, 15)
'''
kernel = np.ones((15, 15))
kernel = kernel / np.sum(kernel)

f2d = cv2.filter2D(image, ddepth=cv2.CV_8U, kernel=kernel)
cv2.imshow('Filter', f2d)
cv2.waitKey(0)

## Guassian
'''for GaussianBlur, ksize value must be an odd int'''
guas = cv2.GaussianBlur(image, ksize=(15, 15), sigmaX=5, sigmaY=5)
cv2.imshow('Filter', guas)
cv2.waitKey(0)



# Non-linear filter 

## medianBlur
'''Smoothes an image by median filter with ksize x ksize'''
'''中值滤波，即取范围内的均值作为结果。效果是将去除图片中差异值，
   使得图片出现大片的同色区域，但不会模糊边界'''
medi = cv2.medianBlur(image, ksize=9)
cv2.imshow('Filter', medi)
cv2.waitKey(0)


## Sobel filter
'''In Sobel, the ksize must be one of 1, 3, 5 and 7'''
'''Sobel 计算的是图像的'''
sobe = cv2.Sobel(image, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=3)
cv2.imshow('Filter', sobe)
cv2.waitKey(0)


### Sobel edge
s1 = cv2.Sobel(image, ddepth=cv2.CV_8U, dx=1, dy=0, ksize=3)
s2 = cv2.Sobel(image, ddepth=cv2.CV_8U, dx=0, dy=1, ksize=3)
'''mean of s1 and s2'''
dst = cv2.addWeighted(s1, 0.5, s2, 0.5, 0)
cv2.imshow('Filter', dst)
cv2.waitKey(0)

## bilateralFilter
'''
双边滤波： 同时考虑像素值差别和空间距离，两个像素差别越小，权重越大；两个像素距离越近，权重越大
位置距离权重：
    w1 = exp(-1 * ( (x-i)^2 + (y-j)^2 ) / (2*e^2) ) 
像素差异权重：
    w2 = exp(-1 * (f(x,y)-f(i,j))^2 / (2*e^2) )
    weight = w1 * w2
因此，在边缘位置时，像素距离近但差异大，使得weight变小，从而保持了清晰的细节
'''

bila = cv2.bilateralFilter(image, d=25, sigmaColor=1, sigmaSpace=1)
cv2.imshow('Filter', bila)
cv2.waitKey(0)

cv2.destroyAllWindows()

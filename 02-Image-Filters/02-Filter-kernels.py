import cv2
import numpy as np

image=cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
cv2.namedWindow('Origin', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Origin', image)

# filter2D

# this kernel will sharp the image
k1 = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
    ])
f1 = cv2.filter2D(image, ddepth=cv2.CV_8U,  kernel=k1)
cv2.namedWindow('K1', cv2.WINDOW_AUTOSIZE)
cv2.imshow('K1', f1)

# this kernel will find the bright edge
k2 = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
f2 = cv2.filter2D(image, ddepth=cv2.CV_8U,  kernel=k2)
cv2.namedWindow('K2', cv2.WINDOW_AUTOSIZE)
cv2.imshow('K2', f2)


# this kernel will find the dark edge
k3 = np.array([
        [1, 1, 1],
        [1,-8, 1],
        [1, 1, 1]
    ])
f3 = cv2.filter2D(image, ddepth=cv2.CV_8U,  kernel=k3)
cv2.namedWindow('K3', cv2.WINDOW_AUTOSIZE)
cv2.imshow('K3', f3)


k4 = np.array([
        [-2, -1, 0],
        [-1,  1, 1],
        [ 0,  1, 2]
    ])
f4 = cv2.filter2D(image, ddepth=cv2.CV_8U,  kernel=k4)
cv2.namedWindow('K4', cv2.WINDOW_AUTOSIZE)
cv2.imshow('K4', f4)

cv2.waitKey(0)
cv2.destroyAllWindows()

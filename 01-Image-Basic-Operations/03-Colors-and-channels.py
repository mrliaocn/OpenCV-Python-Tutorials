import cv2
import numpy as np

image = cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
cv2.namedWindow('Color', cv2.WINDOW_AUTOSIZE)

# Color
# in opencv, image is BGR mode, not RGB.
# set blue and green to 0, and the copy would be red.
copy = np.copy(image)
copy[:,:,0] = 0 # Blue
copy[:,:,1] = 0 # Green
cv2.imshow('Color', copy)
cv2.waitKey(0)

# Convert color
# COLOR_BGR2GRAY: BGR => Gray
# Gray = 0.299⋅R + 0.587⋅G + 0.114⋅B
# about code, see more at https://docs.opencv.org/3.3.1/d7/d1b/group__imgproc__misc.html#ga4e0972be5de079fed4e3a10e24ef5ef0
gray = cv2.cvtColor(image, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('Color', gray)
cv2.waitKey(0)


# Channel Operate
b, g, r = cv2.split(image)
# Merge the channels with reverse order
revs = cv2.merge((r, g, b))
cv2.imshow('Color', revs)
cv2.waitKey(0)

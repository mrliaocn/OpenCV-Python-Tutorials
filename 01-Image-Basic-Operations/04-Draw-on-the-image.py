import cv2
import numpy as np

image = np.zeros((200,200,3),np.uint8)
cv2.namedWindow('Draw', cv2.WINDOW_AUTOSIZE)

# Line
img1 = np.copy(image)
# lineType:
#   LINE_4 : 4-connected line
#   LINE_8 : 8-connected line
#   LINE_AA: antialiased line
cv2.line(img1, (30,30), (100,150), color=(0,0,255), thickness=3, \
    lineType=cv2.LINE_AA)
cv2.imshow('Draw', img1)
cv2.waitKey(0)


# Marker
# About markerType see more at https://docs.opencv.org/3.3.1/d6/d6e/group__imgproc__draw.html#ga0ad87faebef1039ec957737ecc633b7b
img2 = np.copy(image)
# Notice: in this function, the 'line_type' can NOT be written 'lineType', it's may be a mistake of opencv.
cv2.drawMarker(img2, position=(100,100), color=(0,0,255), markerType=cv2.MARKER_DIAMOND,\
    thickness=2, line_type=cv2.LINE_AA, markerSize=10)
cv2.imshow('Draw', img2)
cv2.waitKey(0)


# Circle
img3 = np.copy(image)
cv2.circle(img3, center=(100,100), radius=20, color=(0,0,255), thickness=2, \
    lineType=cv2.LINE_AA)
cv2.imshow('Draw', img3)
cv2.waitKey(0)


# Ellipse

img4 = np.copy(image)
cv2.ellipse(img4, center=(100, 100), axes=(20, 40), angle=20, startAngle=0.0, \
    endAngle=360.0, color=(0, 0, 255), thickness=-1);
cv2.imshow('Draw', img4)
cv2.waitKey(0)


# Rectangle
img5 = np.copy(image)
cv2.rectangle(img5, pt1=(50, 50), pt2=(180, 120), color=(0, 0, 255), thickness=2, \
    lineType=cv2.LINE_AA);
cv2.imshow('Draw', img5)
cv2.waitKey(0)


# Polygon
img6 = np.copy(image)
points = [(50, 50),(80, 20),(120, 30), (150,90),(100,80)]
cv2.fillConvexPoly(img6, points=np.array(points), color=(0, 0, 255), \
    lineType=cv2.LINE_AA);
cv2.imshow('Draw', img6)
cv2.waitKey(0)


# Text
img7 = np.copy(image)
font = cv2.FONT_HERSHEY_SIMPLEX
# org: The bottom-left corner of the text string in the image.
cv2.putText(img7, text="opencv", org=(10,100), fontFace=font, \
    fontScale=1, color=(0,0,255), thickness=2 )
cv2.imshow('Draw', img7)
cv2.waitKey(0)

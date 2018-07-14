import cv2

gogopher = cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
puppy = cv2.imread('../assets/puppy.jpg', flags=cv2.IMREAD_COLOR)

cv2.namedWindow('TrackerBar', cv2.WINDOW_AUTOSIZE)

def on_tracker(val):
    alpha = val / 100
    dst = cv2.addWeighted(gogopher, alpha, puppy, 1 - alpha, 0)
    cv2.imshow('TrackerBar', dst)

on_tracker(35)
# createTrackbar(tracker_name, window_name, display_value, max_value, handler)
cv2.createTrackbar('AlphaTracker', 'TrackerBar', 35, 100, on_tracker)
# The min value of tracker is default 0.
# but you can set the min by setTrackbarMin()
cv2.setTrackbarMin('AlphaTracker', 'TrackerBar', 20)

# set current value
# cv2.setTrackbarPos('AlphaTracker', 'TrackerBar', 35)

# set max value
# cv2.setTrackbarMax('AlphaTracker', 'TrackerBar', 100)

cv2.waitKey(0)

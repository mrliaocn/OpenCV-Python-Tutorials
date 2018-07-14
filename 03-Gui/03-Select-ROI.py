import cv2

gogopher = cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
cv2.namedWindow('Origin', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Origin', gogopher)

cv2.namedWindow('ROI', cv2.WINDOW_AUTOSIZE)

while True:
    x, y, w, h = cv2.selectROI('Origin', gogopher, showCrosshair=True, fromCenter=False)
    # init the value in case got 0.
    if w * h is 0:
        w = h = 200
    ROI = gogopher[y:y+h, x:x+w, :]
    cv2.imshow('ROI', ROI)
    # Press Q to quit.
    print('================================================\n\nPress Q to quit, any others to reset.\n')
    if cv2.waitKey(0) == ord('q'):
        exit(0)

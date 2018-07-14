import cv2

gogopher = cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
cv2.namedWindow('Mouse', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Mouse', gogopher)

# about event, see more at https://docs.opencv.org/3.3.1/d7/dfc/group__highgui.html#ga927593befdddc7e7013602bca9b079b0
# about flags, see more at https://docs.opencv.org/3.3.1/d7/dfc/group__highgui.html#gaab4dc057947f70058c80626c9f1c25ce
def on_mouse(event, x, y, flags, userdata):
    if event is cv2.EVENT_MOUSEMOVE:
        print('Mouse moves to (%d, %d)' %(x, y))
    elif event is cv2.EVENT_LBUTTONDOWN:
        print('Left click down at (%d, %d)' %(x, y))
    elif event is cv2.EVENT_RBUTTONDOWN:
        print('Left click down at (%d, %d)' %(x, y))
    elif event is cv2.EVENT_LBUTTONUP:
        print('Relase left at (%d, %d)' %(x, y))
    # EVENT_MOUSEWHEEL: for up and down only
    elif event is cv2.EVENT_MOUSEWHEEL:
        delta = cv2.getMouseWheelDelta(flags)
        pixels = delta * 120
        print('Scrolled %d px' % pixels)

cv2.setMouseCallback('Mouse', on_mouse)

cv2.waitKey()

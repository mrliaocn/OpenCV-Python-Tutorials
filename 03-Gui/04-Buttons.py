# NOT WORK CURRENTLY !!!
# YOU SHOULD USE PyQt FOR THE BUTTON CONTROL INSTEAD OF OpenCV GUI.



# import cv2

# gogopher = cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
# cv2.namedWindow('Button', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('Button', gogopher)

# b, g, r = cv2.split(gogopher)

# def on_click(state, userdata):
#     if userdata is 'blue':
#         cv2.imshow('Button', b)
#         cv2.setWindowTitle('Button', 'Blue Channel')

#     elif userdata is 'green':
#         cv2.imshow('Button', g)
#         cv2.setWindowTitle('Button', 'Green Channel')

#     elif userdata is 'red':
#         cv2.imshow('Button', r)
#         cv2.setWindowTitle('Button', 'Red Channel')

# cv2.createButton('Blue', on_click, 'blue', cv2.QT_PUSHBUTTON)
# cv2.createButton('Green', on_click, 'green', cv2.QT_PUSHBUTTON)
# cv2.createButton('Red', on_click, 'red', cv2.QT_PUSHBUTTON)

# cv2.waitKey(0)

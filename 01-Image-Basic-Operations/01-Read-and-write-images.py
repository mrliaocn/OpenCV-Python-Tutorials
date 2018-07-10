import cv2

# Read the image
# About flags: see more in https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80
# IMREAD_UNCHANGED = -1
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR     = 1
# IMREAD_ANYDEPTH  = 2
# IMREAD_ANYCOLOR  = 4
# IMREAD_LOAD_GDAL = 8
image=cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
print('shape:', image.shape) # H * W * C
print('size:', image.size)
print('dtype:', image.dtype)

# Create a window named 'Image'
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)

# Show the image in the window
cv2.imshow('Image', image)

# Wait for user input and quit
cv2.waitKey(0)
# Manually destroy the window
cv2.destroyWindow('Image')
# Or:
# cv2.destroyAllWindows()
cv2.imwrite('./copied.jpg', image)

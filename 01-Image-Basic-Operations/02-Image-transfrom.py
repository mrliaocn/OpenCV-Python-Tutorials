import cv2
import numpy as np

image  = cv2.imread('../assets/gogopher.jpg', flags=cv2.IMREAD_COLOR)
height = image.shape[0]
width  = image.shape[1]

cv2.namedWindow('Transform', cv2.WINDOW_AUTOSIZE)

# Resize
# About interpolation see more in https://docs.opencv.org/3.3.1/da/d54/group__imgproc__transform.html#ga5bb5a1fea74ea38e1a5445ca803ff121
# INTER_NEAREST       = 0
# INTER_LINEAR        = 1
# INTER_CUBIC         = 2
# INTER_AREA          = 3
# INTER_LANCZOS4      = 4
# INTER_MAX           = 7
# WARP_FILL_OUTLIERS  = 8
# WARP_INVERSE_MAP    = 16
resize = cv2.resize(image, (height*2, width*2), interpolation=cv2.INTER_NEAREST)
cv2.imshow('Transform', resize)
cv2.waitKey(0)


# Translation
# dst(x,y)=src(M11⋅x+M12⋅y+M13, M21⋅x+M22⋅y+M23)

# In this example:
#   tran[x, y] = iamge[x+100, y+5]
# The image moves 100 pixels right, and 5 pixels down.
M = np.float32([[1,0,100],[0,1,5]])
tran = cv2.warpAffine(image, M, (height, width))
cv2.imshow('Transform', tran)
cv2.waitKey(0)


# Rotate
# Calculates an affine matrix of 2D rotation. 
#   getRotationMatrix2D(center, angle, scale)
# see more at https://docs.opencv.org/3.3.1/da/d54/group__imgproc__transform.html#gafbbc470ce83812914a70abfb604f4326
M = cv2.getRotationMatrix2D((height/2, width/2), 10, 1)
rota = cv2.warpAffine(image, M, (height, width))
cv2.imshow('Transform', rota)
cv2.waitKey(0)

# Affine transform
# transform point src position to dst position
# See more at https://docs.opencv.org/3.3.1/da/d54/group__imgproc__transform.html#ga8f6d378f9f8eebb5cb55cd3ae295a999
src = np.float32([[50,50],[0,100],[10,0]])
dst = np.float32([[50,50],[50,20],[10,0]])
M = cv2.getAffineTransform(src, dst)
affi = cv2.warpAffine(image, M, (height, width))
cv2.imshow('Transform', affi)
cv2.waitKey(0)

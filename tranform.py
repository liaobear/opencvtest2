import cv2
import numpy as np

img = cv2.imread('./image/san.jpg')
img = cv2.resize(img,(305,305))
rows,cols,channel = img.shape
M = cv2.getRotationMatrix2D(((cols - 1) / 2, (rows - 1) / 2),45,2)
dst = cv2.warpAffine(img,M,(rows * 2, cols * 2))

cv2.imshow('img',img)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
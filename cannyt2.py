import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img = cv2.imread('./image/san.jpg', 0)
img = cv2.resize(img,(800,600))
img = cv2.GaussianBlur(img,(5,5),0)


cv2.imshow('image',img)
cv2.createTrackbar('min','image',0,255,nothing)
cv2.createTrackbar('max','image',0,255,nothing)
while(True):
    min = cv2.getTrackbarPos('min','image')
    max = cv2.getTrackbarPos('max','image')
    edges = cv2.Canny(img, min, max)
    cv2.imshow('canny',edges)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()    
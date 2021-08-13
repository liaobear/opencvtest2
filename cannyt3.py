import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img = cv2.imread('./image/san.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(5,5),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


cv2.imshow('image',img)
cv2.createTrackbar('min','image',0,255,nothing)
cv2.createTrackbar('max','image',0,255,nothing)
while(True):
    min = cv2.getTrackbarPos('min','image')
    max = cv2.getTrackbarPos('max','image')
    edges = cv2.Canny(gray, min, max)
    dst = cv2.bitwise_and(img,img,mask=edges)
    cv2.imshow('canny',edges)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()  
import cv2
# 用灰度模式加载图像
img = cv2.imread('./image/san.jpg', cv2.IMREAD_COLOR)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
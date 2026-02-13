import cv2;
import numpy as np;

img = cv2.imread("image.png")

#hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])

lower_red1 = np.array([170,120,70])
upper_red1 = np.array([180,255,255])

#create mask
mask1 = cv2.inRange(hsv,lower_red,upper_red)
mask2 = cv2.inRange(hsv,lower_red1,upper_red1)
mask = mask1 + mask2

cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2;
import numpy as np;

img = cv2.imread("image.png")
#HSV
#h - Hue(color type)
#s - Saturation(color intensity)
#v - Value(color brightness)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

#cv2.imshow("HSV",hsv)
#cv2.imshow("H",h)
#cv2.imshow("S",s)
cv2.imshow("V",v)
cv2.waitKey(0)
cv2.destroyAllWindows()

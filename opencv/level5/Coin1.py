import cv2
import numpy as nx_pydot

#load image
img = cv2.imread("coin.jpeg")

#gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#blur using gussian blur
blur = cv2.GaussianBlur(gray, (5,5), 0)
# cv2.imshow("Blur", blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#edge detection using canny
edges = cv2.Canny(blur,50,150)
# cv2.imshow("Edges", edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#coutours
countours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt =0
for c in countours:
    cnt += 1

print(cnt)    
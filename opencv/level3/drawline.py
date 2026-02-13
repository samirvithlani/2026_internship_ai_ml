import cv2

img = cv2.imread("image.png")

#draw line
#starting point, ending point, color, thickness
cv2.line(img,(50,50),(200,50),(255,0,0),5)

#rectangle
cv2.rectangle(img,(0,250),(200,200),(0,255,0),5)
#circle
#starting point, radius, color, thickness
cv2.circle(img,(250,250),50,(0,0,255),5)

cv2.imshow("line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
img = cv2.imread("image.png")

h,w,c = img.shape
print(h,w,c)

#resize
# resized =  cv2.resize(img,(400,600))
# cv2.imshow("resized",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#crop

# cropped = img[0:300,0:300]
# cv2.imshow("cropped",cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#rotate
# center = (w//2,h//2)
# matrix = cv2.getRotationMatrix2D(center,90,1)
# rotated = cv2.warpAffine(img,matrix,(w,h))
# cv2.imshow("rotated",rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#flipp
#flipped = cv2.flip(img,0) #vertical 
#flipped = cv2.flip(img,1) #horizontal
flipped = cv2.flip(img,-1) #both
cv2.imshow("flipped",flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("flipped.png",flipped)

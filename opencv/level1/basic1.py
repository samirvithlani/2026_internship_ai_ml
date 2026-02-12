import cv2
img = cv2.imread("image.png")
# cv2.imshow("My Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(type(img))
print(img.shape) 
#(2053,1063,3)
#2053 -> height
#1063 -> width
#3 -> channels -->BGR

#blue channel
# blue = img[:,:,0]
# cv2.imshow("Blue",blue)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

red = img[:,:,2]
cv2.imshow("Red",red)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,w = red.shape
print(h,w)
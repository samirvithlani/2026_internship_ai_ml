import cv2

# Read image
img = cv2.imread("example-of-2d-shapes.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    area = cv2.contourArea(cnt)

    # Ignore small noise
    if area > 400:

        # Perimeter
        peri = cv2.arcLength(cnt, True)

        # Approximate shape
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        corners = len(approx)
        print(corners)
        x, y, w, h = cv2.boundingRect(approx) # x, y is the top-left corner of the bounding box

        if corners == 3:
            shape = "Triangle"
        elif corners == 4:
            shape = "Rectangle"
        elif corners == 5:
            shape = "Pentagon"
        else:
            shape = "Circle"


        

        # -------- DRAW SHAPE --------
        if corners > 6:
            (cx, cy), radius = cv2.minEnclosingCircle(cnt)
            center = (int(cx), int(cy))
            radius = int(radius)
            cv2.circle(img, center, radius, (0, 0, 255), 5)
            cv2.putText(img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)
            cv2.putText(img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Show final result
cv2.imshow("Shape Detection System", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

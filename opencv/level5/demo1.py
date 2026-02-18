import cv2
import numpy as np

# Open webcam using DirectShow (important for Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

# Drawing canvas
canvas = None

prev_x, prev_y = None, None

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Camera not opened")
        continue   # don't break, just skip frame
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Skin color range (works in normal lighting)
    lower_skin = np.array([0, 30, 60])
    upper_skin = np.array([20, 150, 255])

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    

    # Morphology to clean noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)

        if area > 800:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            center = (int(x), int(y))

            # Draw tracking circle
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

            if prev_x is None and prev_y is None:
                prev_x, prev_y = center
            else:
                cv2.line(canvas, (prev_x, prev_y), center, (0, 0, 255), 5)
                prev_x, prev_y = center
        else:
            prev_x, prev_y = None, None
    else:
        prev_x, prev_y = None, None

    # Merge drawing with live frame
    combined = cv2.add(frame, canvas)

    cv2.imshow("🎨 Air Drawing - Press ESC to Exit | C to Clear", combined)

    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break
    elif key == ord('c'):
        canvas = np.zeros_like(frame)

cap.release()
cv2.destroyAllWindows()

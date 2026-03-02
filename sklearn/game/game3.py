import cv2
import numpy as np

# Grid size
rows = 3
cols = 3
tile_size = 120

# 0 = empty tile
board = [
    1, 2, 3,
    4, 5, 6,
    7, 0, 8
]

def draw_board():
    img = np.ones((rows*tile_size, cols*tile_size, 3), dtype=np.uint8) * 255

    for i in range(rows * cols):
        r, c = divmod(i, cols)
        x = c * tile_size
        y = r * tile_size

        if board[i] != 0:
            cv2.rectangle(img, (x, y), (x+tile_size, y+tile_size), (200,200,200), -1)
            cv2.rectangle(img, (x, y), (x+tile_size, y+tile_size), (0,0,0), 2)

            cv2.putText(img, str(board[i]),
                        (x+40, y+70),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (0,0,0), 3)

        else:
            cv2.rectangle(img, (x, y), (x+tile_size, y+tile_size), (255,255,255), -1)
            cv2.rectangle(img, (x, y), (x+tile_size, y+tile_size), (0,0,0), 2)

    return img

def is_adjacent(i1, i2):
    r1, c1 = divmod(i1, cols)
    r2, c2 = divmod(i2, cols)

    return (abs(r1 - r2) == 1 and c1 == c2) or \
           (abs(c1 - c2) == 1 and r1 == r2)

def mouse_click(event, x, y, flags, param):
    global board

    if event == cv2.EVENT_LBUTTONDOWN:
        col = x // tile_size
        row = y // tile_size
        clicked = row * cols + col

        empty_index = board.index(0)

        if is_adjacent(clicked, empty_index):
            board[clicked], board[empty_index] = board[empty_index], board[clicked]

cv2.namedWindow("Sliding Demo")
cv2.setMouseCallback("Sliding Demo", mouse_click)

while True:
    img = draw_board()
    cv2.imshow("Sliding Demo", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
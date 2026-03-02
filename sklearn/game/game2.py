import cv2
import numpy as np
import random

# -----------------------------
# Load Image
# -----------------------------
img = cv2.imread("original.jpg")

if img is None:
    print("Image not found!")
    exit()

rows = int(input("Enter rows (e.g. 3): "))
cols = int(input("Enter cols (e.g. 3): "))

h, w, _ = img.shape
piece_h = h // rows
piece_w = w // cols

# -----------------------------
# Split Image into Pieces
# -----------------------------
pieces = []

for i in range(rows):
    for j in range(cols):
        piece = img[i*piece_h:(i+1)*piece_h,
                    j*piece_w:(j+1)*piece_w]
        pieces.append(piece)

# Remove last piece (empty tile)
empty_tile = np.ones((piece_h, piece_w, 3), dtype=np.uint8) * 255
pieces[-1] = empty_tile

# Create board indices
board = list(range(rows * cols))
random.shuffle(board)

move_count = 0


# -----------------------------
# Draw Puzzle
# -----------------------------
def draw_puzzle():
    rows_list = []

    for i in range(rows):
        row_imgs = []
        for j in range(cols):
            idx = board[i*cols + j]
            row_imgs.append(pieces[idx])
        rows_list.append(np.hstack(row_imgs))

    puzzle = np.vstack(rows_list)

    # Draw grid
    for i in range(1, rows):
        cv2.line(puzzle, (0, i*piece_h), (w, i*piece_h), (0,0,0), 2)

    for j in range(1, cols):
        cv2.line(puzzle, (j*piece_w, 0), (j*piece_w, h), (0,0,0), 2)

    cv2.putText(puzzle, f"Moves: {move_count}",
                (10, h-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255,0,0), 2)

    return puzzle


# -----------------------------
# Get Index from Mouse
# -----------------------------
def get_index(x, y):
    col = x // piece_w
    row = y // piece_h
    return row * cols + col


# -----------------------------
# Check if Adjacent to Empty
# -----------------------------
def is_adjacent(i1, i2):
    r1, c1 = divmod(i1, cols)
    r2, c2 = divmod(i2, cols)

    return (abs(r1-r2) == 1 and c1 == c2) or \
           (abs(c1-c2) == 1 and r1 == r2)


# -----------------------------
# Mouse Control
# -----------------------------
def mouse_callback(event, x, y, flags, param):
    global move_count

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = get_index(x, y)
        empty_index = board.index(rows*cols - 1)

        if is_adjacent(clicked, empty_index):
            board[clicked], board[empty_index] = \
                board[empty_index], board[clicked]
            move_count += 1


cv2.namedWindow("Sliding Puzzle")
cv2.setMouseCallback("Sliding Puzzle", mouse_callback)

# -----------------------------
# Game Loop
# -----------------------------
while True:
    puzzle = draw_puzzle()

    # Check solved
    if board == list(range(rows*cols)):
        cv2.putText(puzzle, "DONE 🎉",
                    (w//3, h//2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0,255,0), 3)

    cv2.imshow("Sliding Puzzle", puzzle)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
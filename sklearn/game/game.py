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

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

h, w, _ = img.shape
piece_h = h // rows
piece_w = w // cols

# -----------------------------
# Split Image
# -----------------------------
pieces = []
for i in range(rows):
    for j in range(cols):
        piece = img[i*piece_h:(i+1)*piece_h,
                    j*piece_w:(j+1)*piece_w]
        pieces.append(piece)

shuffled = pieces.copy()
random.shuffle(shuffled)

selected_index = None
move_count = 0


# -----------------------------
# Draw Puzzle
# -----------------------------
def draw_puzzle():
    rows_list = []
    for i in range(rows):
        row_pieces = shuffled[i*cols:(i+1)*cols]
        rows_list.append(np.hstack(row_pieces))

    puzzle = np.vstack(rows_list)

    # Draw grid
    for i in range(1, rows):
        cv2.line(puzzle, (0, i*piece_h), (w, i*piece_h), (0,0,0), 2)

    for j in range(1, cols):
        cv2.line(puzzle, (j*piece_w, 0), (j*piece_w, h), (0,0,0), 2)

    # Highlight selected
    if selected_index is not None:
        r = selected_index // cols
        c = selected_index % cols

        cv2.rectangle(
            puzzle,
            (c*piece_w, r*piece_h),
            ((c+1)*piece_w, (r+1)*piece_h),
            (0,255,0),
            3
        )

    cv2.putText(puzzle, f"Moves: {move_count}",
                (10, h-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255,0,0), 2)

    cv2.putText(puzzle, "Right Click = Rotate",
                (w-300, h-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0,0,255), 2)

    return puzzle


# -----------------------------
# Get Piece Index
# -----------------------------
def get_piece_index(x, y):
    col = x // piece_w
    row = y // piece_h
    return row * cols + col


# -----------------------------
# Mouse Control
# -----------------------------
def mouse_callback(event, x, y, flags, param):
    global selected_index, move_count

    # LEFT CLICK - Start Drag
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_index = get_piece_index(x, y)

    # LEFT RELEASE - Drop
    elif event == cv2.EVENT_LBUTTONUP:
        target_index = get_piece_index(x, y)

        if selected_index is not None and target_index < len(shuffled):
            shuffled[selected_index], shuffled[target_index] = \
                shuffled[target_index], shuffled[selected_index]

            move_count += 1
            selected_index = None

    # RIGHT CLICK - Rotate
    elif event == cv2.EVENT_RBUTTONDOWN:
        idx = get_piece_index(x, y)
        shuffled[idx] = cv2.rotate(
            shuffled[idx],
            cv2.ROTATE_90_CLOCKWISE
        )
        move_count += 1


cv2.namedWindow("Puzzle")
cv2.setMouseCallback("Puzzle", mouse_callback)

# -----------------------------
# Game Loop
# -----------------------------
while True:
    puzzle = draw_puzzle()

    # Check solved
    solved = True
    for i in range(len(pieces)):
        if not np.array_equal(shuffled[i], pieces[i]):
            solved = False
            break

    if solved:
        cv2.putText(puzzle, "DONE 🎉",
                    (w//3, h//2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0,255,0), 3)

    cv2.imshow("Puzzle", puzzle)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
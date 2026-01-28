import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

N =1025
N = 728
img = np.zeros((N,N), dtype=np.uint8)
cv.line(img, (0,0), (N-1,N-1), (255),1)
# cv.imshow('line', img)
if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()


m = 1024
n = 768
c = 3
cl_img = np.zeros((m,n,3), dtype=np.uint8)
cl_img[10:300,:,0] = 255  # Red channel
cl_img[250:500,:,1] = 255    # Green channel
cl_img[450:700,:,2] = 255    # Blue channel
# cv.imshow('color image', cl_img)
cv.waitKey(0)
cv.destroyAllWindows()

# ====== Chessboard 8x8 ======
cell = 100
rows = 8
cols = 8

board_size = cell * rows

chessboard = np.zeros((board_size, board_size, 3), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            color = [203, 192, 255] 
        elif (i == 3 or i == 4) and (j == 3 or j == 4):
            color = [208, 224, 64]
        #tròn
        elif (i == 0 and j == 0) or (i == 0 and j == 7) or (i == 7 and j == 0) or (i == 7 and j == 7):
            color = [0, 0, 255]
        else:
            color = [0, 0, 0]

        chessboard[
            i*cell:(i+1)*cell,
            j*cell:(j+1)*cell
        ] = color

cv.imshow("...", chessboard)
cv.waitKey(0)
cv.destroyAllWindows()


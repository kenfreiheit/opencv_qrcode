import cv2
import numpy as np

img_file = 'test1.png'
img = cv2.imread(img_file)
img_org = img.copy()

dotimg_file = '89486_b4bk_a0.jpeg'
dotimg = cv2.imread(dotimg_file)
dotimg2 = cv2.resize(dotimg, (10, 10))
imgcell = dotimg2[0:10, 0:10]

h, w, ch = img.shape
cell_size = 10

for now_col in range(10, h - cell_size, cell_size):
    for now_row in range(10, w - cell_size, cell_size):
        b, g, r = img[now_col, now_row]
        if b == 0:
            img[now_col:now_col+cell_size,
                now_row:now_row+cell_size] = imgcell

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

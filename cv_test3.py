import cv2

img = cv2.imread('input.jpg')

h, w, ch = img.shape
alpha = 0.3
img2 = cv2.resize(img, (int(w * alpha), int(h * alpha)))
img3 = cv2.resize(img2, (w, h), interpolation=cv2.INTER_NEAREST)

cv2.imshow('image', img3)

cv2.waitKey(0)  # キー入力待ち
cv2.destroyAllWindows()  # ウインドウを閉じる

import cv2
import numpy as np
from PIL import Image

img1 = cv2.imread('test/1.jpg')
img2 = Image.open('test/2.jpg')

img2 = np.array(img2.resize((200,200)))

r, c, ch = img2.shape
roi = img1[0:r, 0:c]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 100, 225, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img1_fg = cv2.bitwise_and(img2, img2, mask = mask)
#cv2.imshow('mask', mask)
cv2.imshow('mask', mask)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img1_fg', img1_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

faceImg = cv2.imread('faces.jpeg', 1)
hsv = cv2.cvtColor(faceImg, cv2.COLOR_BGR2HSV)
h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow('Split HSV', hsv_split)

ret, min_sat = cv2.threshold(s, 40, 355, cv2.THRESH_BINARY)
cv2.imshow('Set Filter', min_sat)

ret2, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Hue Filter', max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow('Final', final)
cv2.imshow('Original', faceImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

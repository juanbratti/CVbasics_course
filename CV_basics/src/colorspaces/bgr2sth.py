import cv2
import os

bgr_im = cv2.imread(os.path.join('..', '..', 'data', 'parrot.jpg'))

rgb_im = cv2.cvtColor(bgr_im, cv2.COLOR_BGR2RGB)
gray_im = cv2.cvtColor(bgr_im, cv2.COLOR_BGR2GRAY)
hsv_im = cv2.cvtColor(bgr_im, cv2.COLOR_BGR2HSV)

cv2.imshow('bgr', bgr_im)
cv2.imshow('rgb', rgb_im)
cv2.imshow('gray', gray_im)
cv2.imshow('hsv', hsv_im)
cv2.waitKey(0)

# color spaces: https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
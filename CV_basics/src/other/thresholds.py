import cv2
import os

# adaptive threshold is better than global. Threshold is dynamic in the adaptive method.

im = cv2.imread(os.path.join('..', '..', 'data', 'thresholds_example.png'))
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, global_thresh = cv2.threshold(im_gray, 80, 255, cv2.THRESH_BINARY)
adaptive_thresh = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)


cv2.imshow('original', im)
cv2.imshow('global thresholded image', global_thresh)
cv2.imshow('adaptive thresholded image', adaptive_thresh)

cv2.waitKey(0)
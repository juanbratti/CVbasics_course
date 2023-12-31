import cv2 as cv
import os

im = cv.imread(os.path.join('..','..','data','birds.png'))

im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

# threshold is only applied to a gray-scale image
ret, thresh = cv.threshold(im_gray, 127, 255, cv.THRESH_BINARY_INV) # inverses threshold, what was black in normal threshold, is now white.

# contours is only applied to a thresholded image
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # contours is a list of the borders of isolated objects in im

for cnt in contours:
    if cv.contourArea(cnt) >= 200:
        # cv.drawContours(im,cnt,-1,(0, 0, 255), 5) # last argument is thickness
        x1, y1, w, h = cv.boundingRect(cnt)
        cv.rectangle(im, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)


cv.imshow('original', im)
cv.imshow('thresholded',thresh)

cv.waitKey(0)
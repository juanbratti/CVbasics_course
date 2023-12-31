import cv2 as cv
import os

im = cv.imread(os.path.join('..','..','data','whiteboard.jpg'))

# line
cv.line(im, (116, 86), (389, 255), (0, 255, 0), 3) # (x-axis, y-axis)

# rectangle
cv.rectangle(im, (116, 86), (389, 255), (0, 0, 255), 5)

# circle
cv.circle(im, (250, 250), 100, (255, 0, 0), 5)

# text
cv.putText(im, 'Pito', (250, 150), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

cv.imshow('im', im)
cv.waitKey(0)
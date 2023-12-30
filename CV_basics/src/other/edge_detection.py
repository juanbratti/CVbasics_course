import cv2
import os
import numpy as np

im = cv2.imread(os.path.join('..','..','data', 'basketball_player.jpg'))

# canny algorithm for detecting edges
im_edge = cv2.Canny(im, 100, 200)

# dilate the edges to improve visualization
im_edge_dilated = cv2.dilate(im_edge, np.ones((5, 5), dtype=np.int8))

# opposite of dilate
im_edge_erode = cv2.erode(im_edge_dilated, np.ones((5, 5), dtype=np.int8))


cv2.imshow('original', im)
cv2.imshow('edges', im_edge)
cv2.imshow('dilated edges', im_edge_dilated)
cv2.imshow('eroded edges', im_edge_erode)


cv2.waitKey(0)

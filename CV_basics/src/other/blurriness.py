import cv2
import os

img = cv2.imread(os.path.join('..', '..', 'data', 'parrot.jpg'))
k_size = 7

im_blur = cv2.blur(img, (k_size, k_size))
im_gauss_blur = cv2.GaussianBlur(img, (k_size, k_size), 5) # last parameter (5) is the standard deviation of the gaussian kernel used for blurring, 
                                                           # the stronger, the blurriest.
im_med_blur = cv2.medianBlur(img, k_size) # good for removing grain effect in images

cv2.imshow('original', img)
cv2.imshow('normal', im_blur)
cv2.imshow('gaussian', im_gauss_blur)
cv2.imshow('median', im_med_blur)
cv2.waitKey(0)
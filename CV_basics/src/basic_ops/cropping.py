import cv2
import os

img = cv2.imread(os.path.join('..', '..', 'data', 'hydrangea.jpeg'))

print(img.shape)

# (height interval, width interval)
# center is top left.
cropped_img = img[90:357, 324:584]
print(cropped_img.shape)
cv2.imshow('Image Visualizer', img)
cv2.imshow('Image Cropped Visualizer', cropped_img)

cv2.waitKey(0)
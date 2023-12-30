import cv2
import os

# resizing

img = cv2.imread(os.path.join('..', '..', 'data', 'hydrangea.jpeg'))

img_resized = cv2.resize(img, (308, 231)) # (width, height)

# prints (height, width)
print(img.shape)
print(img_resized.shape)

# both windows need to have different names
cv2.imshow('Image Visualizer', img)
cv2.imshow('Image Resized Visualizer', img_resized)
cv2.waitKey(0)



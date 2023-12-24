import cv2
import os

# read image
image_path = os.path.join('..', 'data', 'hydrangea.jpeg')
img = cv2.imread(image_path)

# write image
# cv2.imwrite(os.path.join('..', 'data', 'hydrangea_out.jpeg'), img)

# visualize image

cv2.imshow('Image Visualizer', img)
cv2.waitKey(0) # this function tells opencv to keep the window open until a key is pressed.
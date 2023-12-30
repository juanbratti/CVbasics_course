import cv2

# read webcam
webcam = cv2.VideoCapture(0)

# visualize webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('Webcam Visualizer', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): ## if users presses letter 'q', waitKey returns 0xFF and the while true breaks.
        break

webcam.release()
cv2.destroyAllWindows()
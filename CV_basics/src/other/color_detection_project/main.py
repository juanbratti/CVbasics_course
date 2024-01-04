import cv2 as cv

webcam = cv.VideoCapture(0)
while True:
    ret, frame = webcam.read()

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(frame_gray, 127,255, cv.THRESH_BINARY_INV)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv.contourArea(cnt) >= 200:
            x1,y1,w,h = cv.boundingRect(cnt)
            cv.rectangle(frame,(x1,y1), (x1 + w, y1 + h), (0, 255,0),2)

    cv.imshow("Webcam", frame)
    if cv.waitKey(40) & 0xFF == ord('q'): ## if users presses letter 'q', waitKey returns 0xFF and the while true breaks.
        break

webcam.release()
cv.destroyAllWindows()
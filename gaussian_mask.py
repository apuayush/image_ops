import cv2
import numpy as np

cam = cv2.VideoCapture(0)
#cam.set(cv2.CV_CAP_PROP_FRAME_WIDTH,640)
#cam.set(cv2.CV_CAP_PROP_FRAME_HEIGHT,480)

while 1:
    ret1, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thres = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
    gauss = cv2.adaptiveThreshold(gray, 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    
    cv2.imshow('grayscale', thres)
    cv2.imshow('gaussian', gauss)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
import cv2

# Using Android IP Webcam video .jpg stream (tested) in Python2 OpenCV3

import urllib
import cv2
import numpy as np
import time
import urllib.request

'''
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release() '''


url='http://172.20.4.33:8080/shot.jpg'


while True:
    # Use urllib to get the image from the IP camera
    imgResp = urllib.request.urlopen(url)

    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

    # Finally decode the array to OpenCV usable format ;)
    img = cv2.imdecode(imgNp,-1)


	# put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1)

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Use USB camera and plug it into pcDuino8
#Run this python script like :
# python motion_detector.py     ### detect camera

import argparse
import datetime
import time
import cv2
import gpio

btn_pin = "gpio0"
gpio.pinMode(btn_pin, gpio.INPUT)
camera = cv2.VideoCapture(0)
time.sleep(0.25)

while True:
    current_st = gpio.digitalRead(btn_pin)
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    cv2.imshow("video",frame)
    
    next_st = gpio.digitalRead(btn_pin)
    if current_st ^ next_st :	
        name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        cv2.imwrite(name+".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY),100])
 
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

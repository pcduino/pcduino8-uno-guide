# Camera DIY

As mentioned before, we can use guvcview to capture the stream video as a image. So is it possible to DIY a simple camera?

Sure, and it is very easy!

## Pre-requisites:
* Hardware
 - pcDuino8 Uno
 - USB UVC camera

* Software
 - Ubuntu 14.04
 - Python 2.7.6
 - OpenCV 2.4.11

## Steps

### 1. Connect
To make it simple, I just connect GPIO0 to GND via a Dupont line. Insert or pull out the line to simulate pressing or releasing a button.

![](../images/camera-diy.png)

Note: you should know the status that described as the following table.

|Connection|Status|Logic|
|:---:|:---:|:---:|
|Pull out from GND port, without loading|High level|1|
|Insert to GND port|Low level|0|

### 2. Run

```
$ git clone https://github.com/pcduino/pcduino8-uno-guide
$ cd pcduino8-uno-guide/demo/1.CameraDIY/
$ python camera.py
```
* The window show the video from webcam in realtime.
* Pull out the Dupont line from GND port and insert into GND port again.
* The photo will be saved to the current directory.
* View the photo.
```
$ gpicview
```

### Source code

```python

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
    #read the button status
    current_st = gpio.digitalRead(btn_pin)
    (grabbed, frame) = camera.read()

    if not grabbed:
        break

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("video",frame)
    next_st = gpio.digitalRead(btn_pin)

    #check the button status has been changed
    # if yes, save as a image to local
    if current_st ^ next_st :
        name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        cv2.imwrite(name+".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY),100])

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

```



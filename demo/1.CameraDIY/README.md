# How to use Webcam to take a photo

To make it simple, I just connect GPIO0 to GND via a Dupont line. Insert or pull out the line to simulate pressing or releasing a button. Also I use OpenCV to capture the steam video from the Webcam. 

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
* Use a Dupont line, connect GPIO0 to GND port.
* Plug webcam into usb host on pcDuino8 Uno.

### 2. Run
* Open a Linux termial and run the python script.
```
$ python camera.py
``` 
* The window show the video from webcam in realtime. 
* Pull out the Dupont line from GND port and insert into GND port again.
* The photo will be saved to the current dirctory.
* View the photo.
```
$ gpicview
```

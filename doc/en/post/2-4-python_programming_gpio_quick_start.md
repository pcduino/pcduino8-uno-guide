# Python Programming GPIO Quick Start

Python is a programming language that lets you work more quickly and integrate your systems more effectively. You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.

Python is pre-installed in the pcDuino Ubuntu image. The sample Python code can be downloaded from:
https://github.com/pcduino/python-pcduino

The following steps will tell you how to use Python to control pcDuino8 Uno GPIO.

## Steps
### 1. Install necessary tools
```bash
$ sudo apt-get -y install git vim
```
### 2. Download sample python code
```bash
$ git clone https://github.com/pcduino/python-pcduino.git
```
### 3. Control LED7
```bash
$ cd python-pcduino
$ python python-pcduino/Samples/blink_led/blink_led.py
```
Note:**GPIO13 controls LED1, GPIO19 controls LED6 and GPIO18 controls LED7.**
### 4. Read source code
```python
#!/usr/bin/env python
# blink_led.py
# gpio test code for pcduino ( http://www.pcduino.com )
#
import gpio
import time

led_pin = "gpio18"

#define ms delay
def delay(ms):
    time.sleep(1.0*ms/1000)

#set GPIO as output port
def setup():
    gpio.pinMode(led_pin, gpio.OUTPUT)

#loop
def loop():
    while(1):
        gpio.digitalWrite(led_pin, gpio.HIGH)
        delay(200)
        gpio.digitalWrite(led_pin, gpio.LOW)
        delay(100)

def main():
    setup()
    loop()

main()
```

### 5. Use button to control LED
Connect a button to GPIO0 port and read the button's status as input signal, then control the LED on or off.

Based on the given source code, just add several lines to implement this kind of function.

```python
#!/usr/bin/env python
# blink_led.py
# gpio test code for pcduino ( http://www.pcduino.com )
#
import gpio
import time

led_pin = "gpio18"
btn_pin = "gpio0"

#define ms delay
def delay(ms):
    time.sleep(1.0*ms/1000)

#set GPIO18 as OUTPUT port
#set GPIO0 as INPUT port
def setup():
    gpio.pinMode(led_pin, gpio.OUTPUT)
    gpio.pinMode(btn_pin, gpio.INPUT)

#loop
def loop():
    while(1):
        # read GPIO0 status
        if gpio.digitalRead(btn_pin) :
            gpio.digitalWrite(led_pin, gpio.HIGH)    #turn on
        else :
            gpio.digitalWrite(led_pin, gpio.LOW)     #turn off

def main():
    setup()
    loop()

main()

```

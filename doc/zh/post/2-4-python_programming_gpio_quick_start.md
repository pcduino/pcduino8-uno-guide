# Python编程控制GPIO

Python是一种非常简单易学，但又非常强大的编程语言，拥有高效的高级数据结构，且能够用简单而又高效的方式进行面向对象编程。

接下来将介绍如何使用Python访问pcDuino8 Uno上的GPIO接口。具体步骤如下：

## 1. 安装基本的Python包
进入Ubuntu系统，打开Linux终端，系统默认安装了Python，但还需要安装如下的一些包：
```bash
$ sudo apt-get install python-requests  #安装Request
$ sudo apt-get install python-dev IPython #安装python-dev 和IPython
$ sudo apt-get install python-pip   #安装python-pip
$ sudo pip install pip --upgrade  #升级pip
$ sudo pip install flask  #安装Flask
```
## 2. 下载支持pcDuino的Python测试环境
```bash
$ git clone https://github.com/pcduino/python-pcduino.git  #下载python测试环境。
```
## 3. 测试GPIO
```bash
$ cd python-pcduino
$ python python-pcduino/Samples/blink_led/blink_led.py  # 测试 pcDuino8 Uno上LED7。
```
<img src="../images/io.png" title="IO" width=600>

**查看图中 LED7  是否在闪烁！**

## 4. 查看 blink_led 的 Python 代码
```python
#!/usr/bin/env python
# blink_led.py
# gpio test code for pcduino ( http://www.pcduino.com )
#
import gpio
import time

led_pin = "gpio18"

#定义ms延时
def delay(ms):
    time.sleep(1.0*ms/1000)

#设置GPIO为输出
def setup():
    gpio.pinMode(led_pin, gpio.OUTPUT)

#循环运行
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

## 5. 实现按键控制LED灯
根据上面的Python代码进行修改，创建btn.py，用一个GPIO去控制LED的亮灭。
```bash
$ cd Samples/blink_led/
$ vim btn.py
```

**源代码如下：**
```python
#!/usr/bin/env python
# blink_led.py
# gpio test code for pcduino ( http://www.pcduino.com )
#
import gpio
import time

led_pin = "gpio18"
btn_pin = "gpio0"

#定义ms延时
def delay(ms):
    time.sleep(1.0*ms/1000)

#设置GPIO为输出
def setup():
    gpio.pinMode(led_pin, gpio.OUTPUT)
    gpio.pinMode(btn_pin, gpio.INPUT)
#循环运行
def loop():
    while(1):
        # 读取GPIO0的状态
        if gpio.pinRead(btn_pin) :
            gpio.digitalWrite(led_pin, gpio.HIGH)    #灭灯
        else :
            gpio.digitalWrite(led_pin, gpio.LOW)    #亮灯

def main():
    setup()
    loop()

main()
```

保存后运行：
```bash
$ python btn.py
```

根据上面的接口图，将GPIO0接地，查看LED7的状态；再将GPIO0接3.3V，查看LED7的状态，是否满足程序设计？

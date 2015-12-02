# pcDuino8 Uno介绍

![front](../images/pcduino8_uno_1.jpg)

pcDuino8 Uno是一款高性能，高性价比的卡片式电脑，可运行诸如Ubuntu Linux和Android操作系统。pcDuino8 Uno图形化桌面输出采用HDMI接口，最高支持1080P显示。内置硬件视频处理引擎，支持1080p 60fps 视频解码器和1080p 30fps H.265/HDEV视频编码。pcDuino8 Uno的I/O引脚兼容非常流行的Arduino生态系统，可接入Arduino Shield扩展板；系统自带多种开发工具，如Arduino-IDE，Scratch等编程软件，也可以支持Python、Processing等编程。

该开源板迎合了开源社区快速增长的需求，既满足了用户对Arduino生态系统兼容的要求，提升了pcDuino开发板的易用程度；又因为带有8核高性能的ARM Core-A7 2.0GHz的处理器，还有丰富的扩展接口，包括音频视频输出接口，摄像头接口，USB接口，极大地扩展了该开发板的应用领域，尤其是视频处理。

<img src ="../images/pcduino8_uno_2.jpg", title="back", width="400">

## 主要特性

### 1. CPU

pcDuino8 Uno采用全志的H8 SoC，CPU基于台积电最新领先的28纳米制造工艺，采用8个ARM Cortex-A7内核，支持8核心同时2.0GHz高速运行。

### 2. GPU

搭配Imagination 旗下强劲的PowerVR SGX544 图像处理架构, 工作频率可达700M左右，支持OpenGL ES2.0/1.1, OpenCL 1.1 API。

### 3. 多媒体处理特性

* 支持多种的1080p@60fps视频处理
* 支持H.265/HEVC格式
* 集成8M ISP图像信号处理架构，可支持800万像素摄像头。

### 4. 视频输出

* HDMI接口输出，支持1080p@60fps显示
* 支持HDCP V1.2协议
* 支持HDMI CEC

### 5. 其他通用接口

* 千兆以太网接口
* 1 x USB
* 1 x USB OTG，可支持OTG-to-Ethernet
* Micro USB 5V，2V直流供电

### 6. Arduino兼容I/O接口

* 14 x GPIO
* 2 x PWM
* 1 x UART
* 1 x SPI
* 1 x I2C
* 6 x ADC(需外接扩展模块)

### 7. 操作系统

* Ubuntu 14.04
*Android 4.4

### 8. 编程工具

* Arduino IDE
* Scratch
* Processing
* Python

## 外部接口分布

<img src ="../images/io.png" title="I/O" width="500">

## pcDuino8 Uno V.S. 树莓派2

|参数|pcDuino8 Uno|树莓派2|
|---|---|---|
|CPU|全志 H8 8-Core Cortex-A7 @ 2.0GHz|博通 BCM2836 4-Core ARM7 @900MHz|
|GPU|Power VR SG544 @720MHz|Dual-Core Videocore IV@250MHz|
|DRAM|DDR3 1GB|DDR2 1GB|
|板上存储|microSD 卡|microSD 卡|
|网络接口|10/100/1000 兆以太网|10/100 兆以太网|
|操作系统|Ubuntu 14，Android|NOOBS,RASPBIAN,Ubuntu Mate, Windows 10 IOT,OSMC 等|
|视频输出|HDMI 1.4，分辨率最高支持 1920x1080|HDMI 1.4，分辨率支持从 640 x 350 至 1920 x 1200|
|GPIO扩展口|兼容 Arduino Uno I/O，包括：14x GPIO, 2xPWM, 1x UART, 1x SPI，1x I2C，6xADC（需外接ADC模块）|40 x GPIO|
|HDMI|1 x HDMI 1.4|1 x HDMI 1.4|
|音频输出|3.5mm 模拟音频接口|3.5mm 模拟音频接口|
|红外接收|红外接收器接口（可安装）|无|
|摄像头|MIPI 接口|CSI 接口|
|USB|1 x USB Host, 1 x USB OTG|4xUSB host|
|电源供电|5V, 2000mA Micro USB|5V, 1000mA Micro USB|
|尺寸|92x54mm | 86x56mm|

## 试用体验

<img src= "../images/pcduino8_uno_4.jpg" title="handon" width="400" >

pcDuino8 Uno 拿在手上，确实小巧，迫不及待地按照网上提供的教程刷了 Ubuntu 14.04 系统。接上显示器，鼠标和键盘，上电启动，10 秒左右，进入系统桌面，这速度真是够可以的。再想想我现在快要淘汰的笔记本，开机速度接近两分钟，这一对比，心中都是泪啊。

既然是 8 核，标称 2.0GHz 的处理器，恨不得将 8 个核全部跑满。于是用来编译 openCV、编译系统内核，完全当作一个编译服务器来用，这时觉得 1G DRAM 还真是不够用啊，编译开个 8 线程（是不是要疯啊），内存就扛不住了。后来装上了 VLC，转播视频流，当作一个视频服务器。再接着用 openCV 做各种图像和视频处理，比如视频监控、摄像头的人脸识别、运动检测等等。试用结果看，pcDuino8 Uno 的性能确实有着很大的优势，但问题来了，如何在程序中充分挖掘多核的性能呢！

<img src="../images/face_detection.png" title="人脸识别" width="300">

<img src="../images/camera.png" title="网络视频监控" width="300">

利用各种开源的项目，在 pcDuino8 Uno 上折腾，乐在其中！


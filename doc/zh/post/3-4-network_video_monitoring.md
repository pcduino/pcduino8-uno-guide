# 如何使用motion实现网络视频监控

pcDuino8 Uno+USB摄像头+开源工具，几分钟搞定远程视频监控！


## 准备
**硬件**
- pcDuino8 Uno Get Started Kit

**软件**
- 预安装了OpenCV的Ubuntu 14.04

## 实现步骤
### 1. 安装软件
```bash
$ sudo apt-get update
$ sudo apt-get install motion
```

### 2.  修改配置文件
``` bash
$ sudo vim /etc/motion/motion.conf
$ chmod 777 /media
```
需要确认下面这些参数：
> daemon on #default off (This allows the motion to run in the background)

> framerate 10 #default 2 (increased framerate)

>width 640 #default 320 (changed width to match that of the webcam)

>height 480 #default 240 (same as above but for height)

> threshold 2000 #default 1500 (*explained in detail below)

> pre_capture 2 #default 0 (captures 2 frames before motion was detected and adds that to the videos to make them smoother)

> post_capture 5 #default 0 (same as above but captures frames after)

> output_normal off #default on (this disables storing images, since we only require video)

> ffmpeg_video_codec msmpeg4 #default swf (msmpeg4 is accepted by windows media player, hence easier to play on Windows)

> target_dir /mnt/motionvideos #default /tmp/motion (changed the directory where videos will be stored)

> webcam_maxrate 5 #default 1 (increase the max framerate on lie stream)

> webcam_localhost off #default on (allows you to set up a live stream of the webcam)

**注意：上面的部分参数需要根据你的摄像头实际参数进行设置**

### 3. 创建目录

我们需要根据上面的target_dir创建一个目录：
```bash
$ sudo mkdir /mnt/motionvideos
$ sudo chown motion /mnt/motionvideos
```

### 4. 修改默认的配置文件，允许后台启动
```bash
$ sudo vi /etc/default/motion
```
将其中的start_motion_daemon= **no** 修改成 **yes**  。

### 5. 插入USB摄像头，确认系统可以识别

```
$ ls /dev/video0
```

### 6. 启动服务
```bash
ubuntu@RPI:~$ sudo service motion start
 * Starting motion detection daemon motion       [ OK ]
 ```
如果要关闭服务，可运行：
```
$ sudo service motion stop
```

##  测试

pcDuino8 Uno接入局域网，获得IP地址。在同一局域网中的一台电脑或手机上，浏览器访问：
** < pcDuino8 Uno IP Address\>:8081**

可看到摄像头播放的视频：

<img src="../images/camera.png" title="camera" width="400">

更多配置信息，见[参考链接](http://sjj.azurewebsites.net/?p=701)。

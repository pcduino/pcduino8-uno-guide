# How to use pcDuino8 Uno to implement Network Video Monitoring

If you have pcDuino8 Uno which is connected to Internet, and also, you have a webcam. Then you can build a network video monitoring system, just several minutes.

Let's start.

## Prerequisites
### 1. Hardware
- OpenCV computer vision kit 

### 2. Software
- motion

## Steps
### 1. Install software

```bash
$ sudo apt-get update
$ sudo apt-get install motion
```

### 2. Modify configuration
```bash
$ sudo vim /etc/motion/motion.conf
```

The following parameters need to be confirmed：
> daemon on #default off (This allows the motion to run in the background)
>
> framerate 10 #default 2 (increased framerate)
>
> width 640 #default 320 (changed width to match that of the webcam)
>
> height 480 #default 240 (same as above but for height)
>
> threshold 2000 #default 1500 (*explained in detail below)
>
> pre_capture 2 #default 0 (captures 2 frames before motion was detected and adds that to the videos to make them smoother)
>
> post_capture 5 #default 0 (same as above but captures frames after)
>
> output_normal off #default on (this disables storing images, since we only require video)
>
> ffmpeg_video_codec msmpeg4 #default swf (msmpeg4 is accepted by windows media player, hence easier to play on Windows)
>
> target_dir /mnt/motionvideos #default /tmp/motion (changed the directory where videos will be stored)
>
>
>webcam_maxrate 5 #default 1 (increase the max framerate on lie stream)
>
> webcam_localhost off #default on (allows you to set up a live stream of the webcam)

**Note: you need change some parameters above which are based on what kind of webcam you choose!**

### 3. Create a directory

According to the configuration of motion, we should create a directory where videos will be stored ：

```bash
sudo mkdir /mnt/motionvideos
sudo chown motion /mnt/motionvideos
```

### 4. Change the default configuration，start motion daemon

```bash
sudo vi /etc/default/motion
```
change from :
> start_motion_daemon= **no**

to:
> start_motion_daemon= **yes**

### 5. Plug the USB webcam
To make sure the webcam has been recognized as /dev/video0 file.

```bash
$ ls /dev/video0
```

### 6. Start service
```bash
linaro@linaro-alip:~$ sudo service motion start
 * Starting motion detection daemon motion       [ OK ]
 ```

If you want to turn off the motion service, you can run:
```sudo service motion stop```

## Test
First to get the pcDuino8 Uno IP address, you should open a Linux terminal and run `ifconfig` to read the information of network, especially the IP address. Then, open an browser on your PC or mobile devices(Smart Phone or tablet), which are in the same LAN. Enter the pcDuino8 Uno IP Address, like:
 **< pcDuino8 Uno IP Address>:8081**

Now, you can watch the video from your webcam via network.

![camera](../images/camera.png)

More configuration parameters of motion ,you can check [here][1]。

The steps are very easy, isn't it?

[1]:http://sjj.azurewebsites.net/?p=701

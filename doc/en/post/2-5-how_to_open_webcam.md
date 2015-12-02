# How to use Webcam

In pcDuino8 Uno Get Started Kit, there is a mini webcam for robot to stream video in real time. It is UVC and can be used with pcDuino8 Uno without installing Linux driver. Many software in Ubuntu can capture the stream video from this webcam, like guvcview, VLC, ffmpeg, and OpenCV.

<img src="../images/webcam.jpg" title="captured screen" width="400">

This tutorial will introduce how to use guvcview to open the webcam.

## Steps

### Connect webcam
Plug the webcam into pcDuino8 Uno, and power on.

![](../images/cam_p8.png)

Open a Linux terminal and run command as follows to make sure the webcam could be recognized as /dev/video0.
```bash
$ ls /dev/video0
```

### Open guvcview
The guvcview is a pre-installed software in Ubuntu for pcDuino8 Uno. Run command as follows:
```bash
$ guvcview
```
<img src="../images/capture.png" title="captured screen" width="400">

If you want to capture the stream video as image or video, you just click the button **Cap. Image** or **Cap. Video**.





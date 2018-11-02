# Video-streaming-acquisition

## Video acquistion Python scripts

* [video_from_camera.py](video_from_camera.py): script to acquire video from a usb camera.
* [video_from_file.py](video_from_file.py): script to acquire video from a file.
* [video_from_ip_cam.py](video_from_ip_cam.py): script to acquire video from am IP camera.
* [video_from_youtube_linux.py](video_from_youtube_linux.py): script to acquire video from Youtube using Linux.
* [video_from_youtube_buffer_linux.py](video_from_youtube_buffer_linux.py): script to acquire video from Youtube using Linux with buffer mechanism to smooth the acquisition.
* [video_from_youtube_windows.py](video_from_youtube_windows.py): script to acquire video from Youtube using Windows. Currently, the processing is sequential, first the video is acquired and stored in a file, and then it is shown.

## FAQ
* How to find out the url from ip camera stream published in Internet. 
  1. In Google Chrome, open a website with an embedded ip camera stream.
  2. Inspect the code of the website.
  3. Select the video frame to highlight the code in the inspection window related to it.
  4. Identify and extract the url of the ip camera stream.
    ![](doc/camera_ip_source_1.png )
* [How to find out the url from an ip camera](http://funvision.blogspot.com/2017/06/opencv-reading-ip-camera-video-stream.html)
  * The best approach is to find your IP camera model on [http://www.ispyconnect.com](http://www.ispyconnect.com/) to obtain the url video stream. Some examples:
    * http://IP:PORT/mjpeg/video.mjpg?counter
    * rtsp://IP:PORT/various url
    * rtsp://IP:PORT/axis-cgi/mjpg/video.cgi
    * http://IP:PORT/mjpg/video.mjpg
  * Verify the url inside the VLC. 
    * Remember that VLC ask for password, but Opencv does not.  Therefore, the user and password must be provided included in the url: `rtsp://username:password@IP:PORT...` . Example
      * rtsp://USER:PASS@xxx.xxx.xxx.xxx/axis-media/media.amp?camera=2
  * Using OpenCV library, use the object `VideoCapture cap("http://IP:PORT/mjpeg/video.mjpg?counter")` to acquire the video.
  * Note: FFMPEG is needed in Linux. 

## Resources
* [OpenCV: Getting Started with Videos](https://docs.opencv.org/3.4.0/dd/d43/tutorial_py_video_display.html)
* [Streamlink](https://github.com/streamlink/streamlink). CLI utility that pipes flash videos from online streaming services to a variety of video players such as VLC. Examples of services: Dailymotion, Livestream, Twitch, UStream, YouTube.
* [sh](https://github.com/amoffat/sh): sh is a full-fledged subprocess replacement for Python for Linux that allows you to call any program as if it were a function.
* [Python Subprocess and Popen with Examples](https://www.poftut.com/python-subprocess-popen-examples/)

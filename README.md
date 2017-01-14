#Cyber-Camera
<i>by Amir Fefer </i><br> <br>
An open source for home surveillance: <br>
Cyber-Cam turns any webcam into a smart security home surveillance system. <br>
Allow you to watch and record video streaming anywhere from a secured (TLS/SSL & HTTP Basic Auth) web interface. <br>
Cyber Cam includes smart protection, which plays alarm, sends email and smartphone notifications when a suspicious ,<br> activity captured. Based on real time movement, face, full/upper-body detection. <br>

#Features 
* Watch your webcam stream from anywhere
* Active protection with email and smartphone notifications based on movement/face/full/upper body detection
* Recrod a video, or take a snapshot
* Auto upload recorded videos to your Dropbox account
* TLS/SSL plus http basic authentication for max security
* Responsive Web UI 
* One direction audio stream - stream your voice from anywhere 
* Auto server initialization by hosts discovery
* Get an email when your public IP address has been changed

#Screenshots

Watch simply on the go: <br><br>
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/screenshot_phone1.png) 
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/screenshot2.png)

Or from your browser<br><br>

#Server initialization by hosts discovery
It's time to forget from starting/stopping the sever manually <br>
The server will start  automatically when all the hosts (e.g your smartphone) do NOT reachable in the local network <br>
plus get server's current IP address via email <br>
Just make a `hosts.txt` file in the main `cyber-camera` directory, <br>
Add  the wanted hosts IP separated by line (make sure each host has a static ip on the local network) <br>
Run the `network.py` script instead of `server.py`.<br>
When your public IP has been changed, an email will be sent with the new IP.

#Installations and Requirements
<b> Windows installer (RC1) is ready for testing! check in release tab </b><br>
Tested on fedora 24 and Windows (7-10)  <br>
Download and install python 2.7.9 (32 bit only)
You can use lower 2.7.x  but without  SSL/TLS support.

For a quick installation [pip](https://pip.pypa.io/en/latest/installing.html) is recommended<br>
Dependencies libraries: <br>
[Flask](http://flask.pocoo.org/docs/0.10/installation/#installation)  <br>
[flask_httpauth](https://flask-httpauth.readthedocs.org/en/latest/)<br>
[numpy 1.9.2](http://sourceforge.net/projects/numpy/files/)<br>
[opencv 2.4](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.11/opencv-2.4.11.exe) (Not tested with opencv3)<br>
[pygame](http://www.pygame.org/download.shtml)<br>
[dropbox](https://www.dropbox.com/developers-v1/core/sdks/python)<br>
[pycrypt](https://pypi.python.org/pypi/pycrypto) <br>
For video recording, it must to copy dll files from opencv directoy `opencv\sources\3rdparty\ffmpeg` to python's directory, and rename
to `opencv_ffmpeg` + `[opencv version e.g 2413]` <br>

It's importent to fill out the conf file, pay attention to comments.
For TLS/SSL support, make server's certificate and a key (optional),  you can follow up the manual in the conf file. <br>
The user's password must be in sha224, you can use a generator like [this](http://www.miniwebtool.com/sha224-hash-generator/) <br>
To run the server under windows, run cmd and type `python server.py` <br>

Congratulation! your webcam transformed into a smart security cam. <br>
Don't forget to  port forward, plus you can use ddns service like [noip](http://www.noip.com/free) (only in non HTTPS) <br>
If you encounter a bug, or have some suggestions, please  let me know by email or open an issue. <br>

amirfefer@gmail.com


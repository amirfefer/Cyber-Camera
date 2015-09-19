#Cyber-Camera
<i>by Amir Fefer </i><br> <br>
Transform your simple web cam to a smart security home surveillance system.  <br>
Watch your webcam anywhere, record a video or take a snapshot, from a secured (TLS/SSL & HTTP Basic Auth) web interface. <br>
Apply a smart protection, which play alarm, send email and smarthphone notifications when a suspicious activity captured. 
The smart protection can be active from anywhere, and based on face/full/upper body detection 

#Features 
* Watch your webcam stream from anywhere
* Active protection with email and smartphone notifications based on face/full/upper body detection
* Recrod a video, or take a snapshot
* Auto sync recorded video to your Dropbox account
* Secure TLS/SSL plus http basic authentication
* responsive Web UI 
* Windows installer will come out soon, stay tuned

#Screenshots

Watch simply on the go: <br><br>
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/stream.png) 
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/cloud.png)
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/online.png)

Or from your browser: <br><br>
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/screenshotDesktop.png?raw=true) <br>
#Installations and Requirements
Tested on Windows 7&8, for linux need some code modification  <br>
Download and install python 2.7.9 (32 bit only)
You can use lower 2.7.x but without SSL/TLS support, not recommended!

For a quick installation you can use  [pip](https://pip.pypa.io/en/latest/installing.html) <br>
Install  [Flask](http://flask.pocoo.org/docs/0.10/installation/#installation), there are some dependencies  <br>
Install [flask_httpauth](https://flask-httpauth.readthedocs.org/en/latest/)<br>
Install [numpy 1.9.2](http://sourceforge.net/projects/numpy/files/)<br>
Install [opencv 2.4](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.11/opencv-2.4.11.exe) (Not tested with opencv3)<br>
Install [pycrypt](https://pypi.python.org/pypi/pycrypto) <br>

Now fill out the conf file, pay attention to comments.
For TLS/SSL support, make server certificate and key (optional),  you can follow up the manual in the conf file.
The user password must be in sha224, you can use a generator like [this](http://www.miniwebtool.com/sha224-hash-generator/) <br>
In cmd run python server.py <br>

Congratulation! your webcam transformed into a smart security cam. <br>
Don't forget to  port forward, plus you can use ddns service like [noip](http://www.noip.com/free) <br>
If you encounter a bug, or have some suggestion, please  let me know by email or open issue. <br>

amirfefer@gmail.com


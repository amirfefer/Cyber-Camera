#Cyber-Camera
<i>by Amir Fefer </i><br> <br>
Transform your simple web cam to a smart security cam <br>
Watch your webcam anywhere record a video or take a snapshot, from a secured (TLS/SSL & HTTP Basic Auth) interface. <br>
Apply a smart protection, which play alarm, send email and smarthphone notifications when a Suspicious activity captured. 
The smart protection can be active from anywhere, and based on face/full body/upper body detection 

#Screenshots
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/stream.jpg) 
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/online.jpg)
![Stream](https://github.com/amirfefer/Cyber-Camera/blob/master/static/record.jpg)

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
Create server certificate and key for TLS (optional),  you can follow up the manual in the conf file.
The user password must be in sha224, you can use a generator like [this](http://www.miniwebtool.com/sha224-hash-generator/)
Run python main.py in command line, 

Congratulation!,  your webcam transformed into a smart security cam. <br>
Don't forget to  port forward in your router config. And you can use ddns service like [noip](http://www.noip.com/free) 
If you encounter a bug, or have some suggestion, please  let me know, or contribute, I'll appreciate it.

amirfefer@gmail.com


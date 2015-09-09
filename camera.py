import cv2
import winsound, sys
import os
import mailer
import logging
from threading import Thread
import time
import config
import datetime
logging.basicConfig(filename='app.log',level=logging.DEBUG)
class VideoCamera(object):
    binary = True
    def __init__(self, config):
        self.config = config
        self.video = cv2.VideoCapture(int(self.config.get('Video')['camera']))
        self.videoWriter = None
        self.online = False
    
    def __del__(self):
        self.video.release()
        
    def finished(self):
        self.video.release()
        
    def start_video(self):
        logging.info('Video recording started at ' + str(datetime.datetime.now()))
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.videoWriter = cv2.VideoWriter(self.config.get('File')['videos'] +'video' +timestr +".avi", cv2.cv.CV_FOURCC('M','J','P','G'), int(self.config.get('Video')['fps']),
               (640,480))

    def start(self,sens, method, mail, sound, notif):
        self.online = False
        logging.info('Active security started at ' + str(datetime.datetime.now()))
        iterator = 0
        count = 0
        before = False
        while True:
            success, image = self.video.read()
            if not success:
                continue
            iterator += 1
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            if method == 'face':
                faceCascade = cv2.CascadeClassifier("faceDetect.xml")
            elif method == 'ubody':
                faceCascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")
            elif method == 'fbody':
                faceCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                flags=0)
            if type(faces) is not tuple:
                print faces
                if before:
                    count += 1
                before = True
            else:
                before = False
                count = 0
            if self.online:
                logging.info('Active security Stopped by user at ' + str(datetime.datetime.now()))
                return
            if count == (6 - sens):
                logging.info('Face Detected! at ' + str(datetime.datetime.now()))
                img = self.get_frame(False)
                if notif:
                    try:
                        logging.info('Sending notification  ' + str(datetime.datetime.now()))
                        mailer.send_notification(self.config)
                    except:
                        logging.warn('Error sending notification  ' + str(datetime.datetime.now()))
                if mail:
                    try:
                        logging.info('Sending email ' + str(datetime.datetime.now()))
                        mailer.sendMessege(img, self.config)
                        return
                    except:
                        logging.info('Error Sending Mail ' + str(datetime.datetime.now()))
                if sound:
                    winsound.PlaySound(self.config.get('Sound')['alarm'], winsound.SND_FILENAME)
                return  
            if iterator==10:
                iterator=0
                count=0

    def endVideo(self):
        self.videoWriter.release()
        
    def get_frame(self,faced,saved=False, video=False, videoStop = False):
        while True:
            success, image = self.video.read()
            if not success:
                continue
            else:
                break
        if video:
            self.videoWriter.write(image)
            cv2.circle(image,(20,20), 15, (0,0,255), -1)
        if faced:
            faceCascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                flags=0)
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            ret, jpeg = cv2.imencode('.jpg', image)
            return (jpeg.tostring())
        ret, jpeg = cv2.imencode('.jpg', image)
        return (jpeg.tostring())

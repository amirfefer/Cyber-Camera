import cv2
import mailer
import logging
import time
import datetime
import pygame

logging.basicConfig(filename='app.log',level=logging.DEBUG)
pygame.mixer.init()


class VideoCamera(object):
    binary = True
    def __init__(self, config):
        self.config = config
        self.video = cv2.VideoCapture(int(self.config.get('Video')['camera']))
        self.videoWriter = None
        self.online = False
        self.recording = False
        self.first_captured = None
    
    def __del__(self):
        self.video.release()
        
    def finished(self):
        self.video.release()

    def start(self,sens, method, mail, sound, notif):
        self.online = False
        logging.info('Active security started at ' + str(datetime.datetime.now()))
        iterator = 0
        repeated = 0
        sequence_capture = False
        self.first_captured = None
        while True:
            success, image = self.video.read()
            if not success:
                continue
            iterator += 1
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if method == 'face':
                faceCascade = cv2.CascadeClassifier("haarcascade/faceDetect.xml")
            elif method == 'ubody':
                faceCascade = cv2.CascadeClassifier("haarcascade/haarcascade_upperbody.xml")
            elif method == 'fbody':
                faceCascade = cv2.CascadeClassifier("haarcascade/haarcascade_fullbody.xml")
            elif method == 'move':
                if self.first_captured is None:
                    self.first_captured = gray
                frameDelta = cv2.absdiff(self.first_captured, gray)
                self.first_captured = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.dilate(thresh, None, iterations=2)
                (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in cnts:
                    if cv2.contourArea(c) < int(self.config.get('Video')['min_movement_object']):
                        continue
                    repeated += 1
                    break
            if method == 'ubody' or method == 'fbody' or method == 'face':
                #TODO export arguments to config file
                faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    flags=0)
                if type(faces) is not tuple:
                    if sequence_capture:
                        repeated += 1
                    sequence_capture = True
                else:
                    sequence_capture = False
                    repeated = 0
            if self.online:
                logging.info('Active security Stopped by user at ' + str(datetime.datetime.now()))
                self.first_captured = None
                return
            if repeated == (6 - sens):
                logging.info('Figure has been Detected at ' + str(datetime.datetime.now()))
                ret, jpeg = cv2.imencode('.jpg', image)
                img = jpeg.tostring()
                if notif:
                    try:
                        logging.info('Sending notification  ' + str(datetime.datetime.now()))
                        mailer.send_notification(self.config)
                    except:
                        logging.warn('Error sending notification  ' + str(datetime.datetime.now()))
                if sound: 
                    pygame.mixer.music.load(self.config.get('Sound')['alarm'])
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue

                if mail:
                    try:
                        logging.info('Sending email ' + str(datetime.datetime.now()))
                        mailer.sendMessege(img, self.config)
                    except:
                        logging.info('Error Sending Mail ' + str(datetime.datetime.now()))
                self.first_captured = None
                return
            if iterator == 10:
                iterator = 0
                repeated = 0

    def record(self,upload, cloud):
        self.recording = True
        logging.info('Video recording started at ' + str(datetime.datetime.now()))
        timestr = time.strftime("%Y%m%d-%H%M%S")
        videoWriter = cv2.VideoWriter(self.config.get('File')['videos'] + 'video' + timestr + ".avi", cv2.cv.CV_FOURCC('M','J','P','G'), int(self.config.get('Video')['fps']),
               (640,480))
        while self.recording:
            while True:
                success, image = self.video.read()
                if not success:
                    continue
                else:
                    break
            if self.recording:
                videoWriter.write(image)
                time.sleep(0.08)
        videoWriter.release()
        if upload:
            f = open(self.config.get('File')['videos'] + 'video' + timestr + ".avi", 'rb')
            data = f.read()
            cloud.upload_file(data, '/video' + timestr + ".avi")

    def playAudio(self):
        pygame.mixer.music.load("audio.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

    def endVideo(self):
        self.recording = False

    def get_frame(self,faced,saved=False, video=False, videoStop = False):
        while True:
            success, image = self.video.read()
            if not success:
                continue
            else:
                break
        if video:
            cv2.circle(image,(20,20), 15, (0,0,255), -1)
        if faced:
            faceCascade = cv2.CascadeClassifier("haarcascade/faceDetect.xml")
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

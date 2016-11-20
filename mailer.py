__author__ = 'amir'
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import datetime

def send_notification(conf):
        _user = conf.get('Mailer')['username']
        _pwd = conf.get('Mailer')['password']
        FROM = conf.get('Mailer')['username']
        TO = [conf.get('Notifications')['bxc'] + '@bxc.io']
        SUBJECT = "Figure Detected"
        date = str(datetime.datetime.utcnow())
        TEXT = "A figure was detected at " + date + " ,image was sent via mail"


        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)


        server = smtplib.SMTP_SSL(conf.get('Mailer')['smtp'], int(conf.get('Mailer')['port']))

        server.login(_user, _pwd)
        server.sendmail(FROM, TO, message)

def sendMessege(img_data, conf):
        _user = conf.get('Mailer')['username']
        _pwd = conf.get('Mailer')['password']

        msg = MIMEMultipart()
        msg['Subject'] = 'Figure Detected!'
        msg['From'] = conf.get('Mailer')['username']
        toList = conf.get('Mailer')['to'].split(",")
        msg['To'] = toList[0]
        FROM = conf.get('Mailer')['username']
        TO = toList

        text = MIMEText("Hi, This figure were captured by Cyber Camera")
        msg.attach(text)
        image = MIMEImage(img_data, _subtype="jpg")
        msg.attach(image)
        server = smtplib.SMTP_SSL(conf.get('Mailer')['smtp'], int(conf.get('Mailer')['port']))
        server.login(_user, _pwd)
        server.sendmail(FROM, TO, msg.as_string())

def send_email_address(data, conf):
        _user = conf.get('Mailer')['username']
        _pwd = conf.get('Mailer')['password']

        msg = MIMEMultipart()
        msg['Subject'] = 'IP address for cyber camera'
        msg['From'] = conf.get('Mailer')['username']
        toList = conf.get('Mailer')['to'].split(",")
        msg['To'] = toList[0]
        FROM = conf.get('Mailer')['username']
        TO = toList

        text = MIMEText("Your IP address has been changed to: " + data)
        msg.attach(text)
        server = smtplib.SMTP_SSL(conf.get('Mailer')['smtp'], int(conf.get('Mailer')['port']))
        server.login(_user, _pwd)
        server.sendmail(FROM, TO, msg.as_string())
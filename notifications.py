import requests
import time

class Notification(object):
    def __init__(self, conf):
        self.app_key = 'a2qemn8dgeqs463dm3oue92zw6d129'
        self.user = conf.get('Notifications')['pushover']

    def send_notification(self):
        title = "Suspicious activity has been discovered "
        body = time.strftime("%c") + " - For more information, please check your email" \
                                     " or visit your Cyber-cam web interface"
        requests.post('https://api.pushover.net/1/messages.json',
                      data={'token': self.app_key, 'user': self.user, 'title': title, 'message': body})

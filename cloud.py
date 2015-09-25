import dropbox
class DropObj(object):
    def __init__(self, conf):
        self.app_key = 'ck2ifx3agl50908'
        self.app_secret = 'w95xtn3ouucj6ru'
        self.token = conf.get('Cloud')['token']
        if self.token != 'none':
            self.client = dropbox.client.DropboxClient(self.token)
        else:
            self.client = None
        self.flow = None
        self.conf = conf

    def get_website(self):
        if self.client is None:
            self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)
            return  self.flow.start()
        return 'http://#'

    def auth(self,key):
        if self.token != 'none':
            self.client = dropbox.client.DropboxClient(self.token)
        else:
            key.strip()
            access_token, user_id = self.flow.finish(key)
            self.conf.write('Cloud', 'token',access_token )
            self.client = dropbox.client.DropboxClient(access_token)

    def upload_file(self,file, name):
        self.client.put_file('/'+name, file)
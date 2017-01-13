__author__ = 'amir'
import ConfigParser
import hashlib
class Configuration(object):
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read("conf.ini")

    def write(self, section, attr, value):
        cfgfile = open("conf.ini",'w')
        self.config.set(section,attr,value)
        self.config.write(cfgfile)
        cfgfile.close()

    def get(self, section):
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    print ("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
    def boolean(self, section, attr):
        return self.config.getboolean(section, attr)

    def encrypt(self, data):
        obj = AES.new(self.get('Encryption')['Key'], AES.MODE_CBC, self.get('Encryption')['iv'])
        return obj.encrypt(data)

    def decrypt(self, data):
       obj = AES.new(self.get('Encryption')['Key'], AES.MODE_CBC, self.get('Encryption')['iv'])
       return obj.decrypt(data)

    def hash(self, str):
        return hashlib.sha224(str).hexdigest()


import sys
import os
import platform
import subprocess
import time
import mailer
import datetime
import config
import logging

from urllib2 import urlopen

ip_address = None
hosts_list = {}
any_device = True
plat = platform.system()
conf = config.Configuration()
logging.basicConfig(filename='app.log',level=logging.DEBUG)

def ping(addr):
    if plat == "Windows":
        args = ["ping", "-n", "1", "-l", "1", "-w", "100", addr]

    elif plat == "Linux":
        args = ["ping", "-c", "1", "-l", "1", "-s", "1", "-W", "1", addr]

    ping = subprocess.Popen(
        args,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    out, error = ping.communicate()
    if '100%' in out:
        hosts_list[addr] = False
    else:
        hosts_list[addr] = True
    print error

scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
lines = hostsFile.readlines()
for line in lines:
    line = line.strip( )
    hosts_list[line] = False
hostsFile.close()

def start_listen():
    power = False
    sub_proc = None
    while True:
        global ip_address
        now = datetime.datetime.now()
        if (int)(now.minute) == 0 or (int)(now.minute) == 30:
            public_ip = urlopen('http://ip.42.pl/raw').read()
            if ip_address != public_ip:
                mailer.send_email_address(public_ip, conf)
                logging.info('sending ip to email at ' + str(datetime.datetime.now()))
                ip_address = public_ip

        for key in hosts_list.keys():
            ping(key)
            time.sleep(1)
        if any(hosts_list.itervalues()) and power:
           logging.info('server killed at  '  + str(datetime.datetime.now()))
           sub_proc.kill()
           power = False
        if not any(hosts_list.itervalues()) and not power:
            logging.info('server started at  ' + str(datetime.datetime.now()))
            sub_proc = subprocess.Popen("python server.py")
            power = True
        time.sleep(10)

if __name__ == "__main__":
    start_listen()





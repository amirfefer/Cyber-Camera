__author__ = 'amirf_000'
import sys
import os
import platform
import subprocess
import time

hosts_list = {}
any_device = True
plat = platform.system()


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
        print "No connection to %s" %addr
        hosts_list[addr] = False
    else:
        print "connection success to %s" %addr
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
        for key in hosts_list.keys():
            ping(key)
            time.sleep(1)
        if any(hosts_list.itervalues()) and power:
           print "kill server"
           sub_proc.kill()
           power = False
        if not any(hosts_list.itervalues()) and not power:
            print "open server"
            sub_proc = subprocess.Popen("python server.py")
            power = True
        time.sleep(10)

if __name__ == "__main__":
    start_listen()





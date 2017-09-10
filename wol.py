#!/usr/bin/python
#!/usr/bin/python3

import socket
import struct
import os
import sys

#This has been created to find out what version of Python is being run
#as the ConfigParser module runs differently between Py v2 & v3
import subprocess

#This is the subprocess which gets and returns the systems Py version
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

if __name__ == '__main__':
    command = 'python -V'.split()
for line in run_command(command):
    line = line [0:10]

#If statement to check the version against a set parameter
py_v = 'Python 2.7'
if line == py_v:
    import ConfigParser
else:
    import configparser
#This is what allows the wol.py file to run with Py v2 or v3
if line == py_v:
    Config = ConfigParser.ConfigParser()
else:
    Config = configparser.ConfigParser()



myconfig = {}


def wake_on_lan(host):
    #This is used to switch on the remote computer via WOL
    global myconfig

    try:
      macaddress = myconfig[host]['mac']

    except:
      return False

    # Checks the address
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 12 + 5:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')

    # Padding
    data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
    send_data = b''

    # Split up
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data,
                             struct.pack('B', int(data[i: i + 2], 16))])

    # Broadcast to the LAN.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, (myconfig['General']['broadcast'], 7))
    return True


def loadConfig():
	#This loads and reads the config file
    global mydir
    global myconfig
    Config
    Config.read(mydir+"/.wol.ini")
    sections = Config.sections()
    dict1 = {}
    for section in sections:
    	options = Config.options(section)

    	sectkey = section
    	myconfig[sectkey] = {}


    	for option in options:
    		myconfig[sectkey][option] = Config.get(section,option)


    return myconfig

def usage():
	print('Usage: wol.py [hostname]')


if __name__ == '__main__':
        mydir = os.path.dirname(os.path.abspath(__file__))
        conf = loadConfig()
        try:

                if sys.argv[1] == 'list':
                        print('Configured Hosts:')
                        for i in conf:
                                if i != 'General':
                                        print('\t',i)
                        print('\n')
                else:
                        if not wake_on_lan(sys.argv[1]):
                                print('Wrong hostname entered')
                        else:
                                print('The magic packet has been sent!')
        except:
                usage()

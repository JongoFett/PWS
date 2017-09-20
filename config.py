#!/usr/bin/python3
#!/usr/bin/python

#This creates the config file used to hold & read the MAC address
#import configparser
import os
import sys
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
    config = ConfigParser.ConfigParser()
else:
    config = configparser.ConfigParser()


#ask user the broadcast address
broad_cast = input("What is your broadcast address? ")

#.ini settings
config['DEFAULT'] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                      'CompressionLevel': '9'}

#This is where the broadcast address is set
config['General'] = {}
config['General']['broadcast'] = broad_cast

#This is where the MAC is set/saved
host_name = input('What would you like to name the system? ')
config[host_name] = {}
host_config = config[host_name]
host_config['mac'] = input('What MAC address? ')     # mutates the parser

#Next stage is to look this based on how many MACs are found on the network
#When get_mac.py is run

with open('.wol.ini', 'w') as configfile:
   config.write(configfile)

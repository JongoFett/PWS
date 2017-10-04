#!/usr/bin/python3
#!/usr/bin/python

#This creates the config file used to hold & read the MAC address
#import configparser
import os
import sys
import subprocess
import csv

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

#If statement to check the version, depending on result c_reader changes it's command
py_v = 'Python 2.7'
if line == py_v:
    c_reader = csv.reader(open('./output/macs.csv', 'rb'), delimiter=',')
else:
    c_reader = csv.reader(open('./output/macs.csv', newline=''), delimiter=',')

#ask user the broadcast address
while True:
    broad_cast = input("If you broadbast address is 192.168.0.255 then 'y'\n")
    if broad_cast == 'y':
        broad_cast = '192.168.0.255'
        break
    else:
        broad_cast = input('What the fuck is it then? ')
        print('Your new broadcast address is '+broad_cast)
        break

#Create & return list of mac address'
col_2 = list(zip(*c_reader))[1]
mac_list = col_2[1::]
#Return one mac & a time & ask to name it
for macs in mac_list[0::]:
    host_name = input('What to call mac {} \n'.format(macs))
    config[host_name] = {}
    host_config = config[host_name]
    host_config['mac'] = macs

#.ini settings
config['DEFAULT'] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                      'CompressionLevel': '9'}

#This is where the broadcast address is set
config['General'] = {}
config['General']['broadcast'] = broad_cast

#Next stage is to look this based on how many MACs are found on the network
#When get_mac.py is run

with open('.wol.ini', 'w') as configfile:
   config.write(configfile)

#!/usr/bin/python3
#!/usr/bin/python

import csv
import re
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

#If statement to check the version, depending on result c_reader changes it's command
py_v = 'Python 2.7'
if line == py_v:
    c_reader = csv.reader(open('./output/macs.csv', 'rb'), delimiter=',')
else:
    c_reader = csv.reader(open('./output/macs.csv', newline=''), delimiter=',')

col_2 = list(zip(*c_reader))[1]
mac_list = col_2[1::]
print(mac_list)

#Trying to get the module to go through one mac & a time and ask what you want to call it.
for macs in mac_list[0::]:
    print(macs)
#    name_mac = input('What would you like to call this mac? ')

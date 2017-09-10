#!/usr/bin/python

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
#print(py_v)
if line == py_v:
    import ConfigParser
else:
    import configparser

#!/usr/bin/python
#This simply attmepts to ping a desired IPv4 address
#Nothing fancy
import os
import platform

#Shows simply what the operating system is
#e.g. Linux, Windows etc.
op_sys = platform.system()

#Asks for the desired IP to ping & then displays it
ip_ping = raw_input("What IP would you like to ping?")

#Depending on the platform the code will run a specific
#ping command
#If the system is not Linux then it will run a simple 'ping [IPv4]'
#otherwise it will run a ping limited to 4 packets
if op_sys != 'Linux':
    os.system("ping " + ip_ping)
else:
    os.system("ping -c 4 " + ip_ping)

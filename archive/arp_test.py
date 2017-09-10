#!/usr/bin/python

import os
import socket
import uuid

name_host = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())
print(name_host)
print(ip_address)
print(uuid._arp_getnode())

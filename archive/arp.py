#!/usr/bin/python
import uuid
import os
import socket

#This Def sets up part of the the MAC finding process
def _arp_getnode():
    #get the MAC on Unix via ARP
    try:
        ip_addr = socket.gethostbyname(socket.gethostname())
    except EnvironmentError:
        return None

if __name__ == "__main__":

    #This is where we're going to try and get the MAC
    return (_find_mac('arp', '-an', [ip_addr], lambda i: -1))

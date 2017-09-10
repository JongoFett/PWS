#!/usr/bin/python3

#This creates the config file used to hold & read the MAC address
import configparser

#ask user the broadcast address
broad_cast = input("What is your broadcast address? ")

#.ini settings
config = configparser.ConfigParser()
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

with open('wol.ini', 'w') as configfile:
   config.write(configfile)

#!/usr/bin/python

import csv
import re

c_reader = csv.reader(open('./output/macs.csv', 'rb'), delimiter=',')

col_2 = list(zip(*c_reader))[1]
mac_list = col_2[1::]
for macs in mac_list:
    print(macs)

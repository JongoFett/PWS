#!/usr/bin/python
import re
import subprocess
import csv

#Process to find currently online media devices
arp_out =subprocess.check_output(['arp','-an'])
re.findall(r"((\w{2,2}\:{0,1}){6})",arp_out)

#Format the output
arp_out = arp_out.replace("? ", "")
arp_out = arp_out.replace("at", "")
arp_out = arp_out.replace("on", "")
arp_out = arp_out.replace("(", "")
arp_out = arp_out.replace(")", "")
arp_out = arp_out.replace("  ", ",")
arp_out = arp_out.replace(" ", ",")
arp_out = arp_out.strip()

#Save to .csv for later
with open('./output/macs.csv', 'wb') as csvfile:
    mac_writer = csv.writer(csvfile, skipinitialspace=True, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    mac_writer.writerow(["addr", "mac_addr", "mode", "misc"])
    mac_writer.writerow([arp_out])

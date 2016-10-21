#!/usr/bin/env python
import socket
import os

os.remove('hosts')
hosts = open('hosts', 'w')

with open("domain.txt", "r") as ins:
    for line in ins:
	if not line.startswith('#') and line.strip():
		try:
			data = socket.gethostbyname(line.strip())
			hosts.write( data + "\t" + line.strip() + "\n")
		except:
			print 'ERROR => ' +  data + '   ' + line 

#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "irc.csec.umiacs.umd.edu"   # IP address or URL
port = 4444     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)

split = data.split("\n")


answer = eval(split[1])




while (split[1]):
	hashed = hashlib.sha256(str(answer)).hexdigest()

	s.send(str(hashed) + "\n")

	data = s.recv(1024)
	print(data)
	split = data.split("\n")
	if (split[1]):
		answer = eval(split[1])

# close the connection
s.close()

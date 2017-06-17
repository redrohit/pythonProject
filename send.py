#!/usr/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_ip="127.0.0.1"
server_port=1234
while True:
	msg=raw_input("enter your message : ")
	s.sendto(msg,(server_ip,server_port))
	print "-----------"
	print s.recvfrom(100)

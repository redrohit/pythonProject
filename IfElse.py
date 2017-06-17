
import os
x=  ''' 
     print "1 to give message:"
     print "2 to reboot my machine:"
     print "3 to open webcam:"
    '''
print x
ch=raw_input()
if ch=='1':
	print "welcome to redhat ,ROHIT GUPTA"
elif ch=='2':
	os.system("reboot")
elif ch=='3':
	os.system("cheese")
else:
	print("wrong input")

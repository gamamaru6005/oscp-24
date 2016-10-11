#!/usr/bin/python

import socket
import sys
if len(sys.argv) <2:
    print "usage: provide a file name and list of ip addresses"
    sys.exit(0)


inusers=(sys.argv[1])
inips=(sys.argv[2])
try:
    sys.argv[3]
except NameError:
    helodom = 'megacorpone.com'
else:
    helodom = (sys.argv[3])
print ("connecting to " +  inips + ' for user ' + inusers + ' with domain ' + helodom + '\r\n')
#print ("checking user " + inusers + '\r\n')
socket.setdefaulttimeout(3)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect((inips,25))
banner=s.recv(1024)
print banner
helocommaand= 'EHELO ' + helodom +'r\n'
helocommaand= 'EHELO megacorpone.com\r\n'
s.send(helocommand.encode())
#s.send('VRFY ' + inusers + '\r\n')
result=s.recv(1024)
print result
s.close()

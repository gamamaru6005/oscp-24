#!/usr/bin/python

import socket
import sys
import optparse

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
try:
        sys.argv[4]
except NameError:
        scanport = 25
else:
        scanport = int(sys.argv[4])
print ("connecting to " +  inips + ' for user ' + inusers + ' with domain ' + helodom + ' to port ' + str(scanport) + '\r\n')
#print ("checking user " + inusers + '\r\n')
#socket.setdefaulttimeout(3)
connSkt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connSkt.settimeout(10)
connSkt.connect((inips,scanport))
connSkt.sendall('\r\n')
data='\r\n'

while True:
  connSkt.sendall('EHELO meagacorpone.com\r\n')
  banner=connSkt.recv(100)
  if not banner:
      break
  connSkt.sendall(data)

#print data

print '[+]' + str(banner)
helocommaand= 'EHELO ' + helodom +'r\n'
helocommaand= 'EHELO megacorpone.com\r\n'
connSkt.send(helocommand.encode())
#s.send('VRFY ' + inusers + '\r\n')
result=connSkt.recv(1024)
print '[+]' + str(result)
connSkt.close()

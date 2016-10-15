#!/usr/bin/python
import sys
import os
import nmap
import json
import csv
import xmltodict
from pprint import pprint

#print "Starting read xml and parse"
if len(sys.argv) < 1:
        print "usage: provide a xml file to convert to json " % (sys.argv[0])
        sys.exit(0)
#print ("Args list : %s " %  sys.argv)
infile =(sys.argv[1])

#nm=nmap.PortScanner()

with open(infile,"rb") as fd:
   # content = fd.read()
    doc = xmltodict.parse(fd)
    jdata = (json.dumps(doc, ensure_ascii=True, indent=4))
    sys.stdout.write(jdata)
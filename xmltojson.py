#!/usr/bin/python
import sys
import os
import nmap
import json
import csv
import xmltodict
from pprint import pprint
from xml.parsers.expat import ExpatError
import untangle

#print "Starting read xml and parse"
if len(sys.argv) < 1:
        print "usage: provide a xml file to convert to json " % (sys.argv[0])
        sys.exit(2)
#print ("Args list : %s " %  sys.argv)
infile =(sys.argv[1])
if "xml" not in infile:
    print "please provide an xml file as input"
    sys.exit(3)
target = infile.replace('xml','json')

outfile = open(target,'w')
outfile.truncate()

with open(infile,"rb") as fd:
   # content = fd.read()
    try:
        #doc = xmltodict.parse(fd)
        doc = untangle.parse(infile)
    except ExpatError:
        print "expat error found"

    jdata = (json.dumps(doc, ensure_ascii=True, indent=4))
    sys.stdout.write(jdata)
    outfile.write(jdata)
#sys.stdout.write( "target is " + target)
outfile.close()
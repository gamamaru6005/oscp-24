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
        print "usage: provide a nmap xml file to convert to a csv " % (sys.argv[0])
        sys.exit(0)
#print ("Args list : %s " %  sys.argv)
infile =(sys.argv[1])

#nm=nmap.PortScanner()

with open(infile,"rb") as fd:
   # content = fd.read()
    doc = xmltodict.parse(fd)
    jdata = (json.dumps(doc, ensure_ascii=True, indent=4))
    sys.stdout.write(jdata)
  #  pprint (jdata)
 #   print "end of data"
    """
    csvread = nm.analyse_nmap_xml_scan(content)
    for row in csv.DictReader(csvread):
        json.dump(row,sys.stdout)
        sys.stdout.write('\n')
    #jsonout = json.dumps ( [ row for row in csvread ])
    #print(nm.csv())
   #json.dump(jsonout)
    """
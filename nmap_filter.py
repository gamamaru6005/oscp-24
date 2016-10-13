#!/usr/bin/python
import sys
import fileinput
import json
import xmltodict
import lxml.objectify
import argparse
import re


parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('-s', action='store', dest='startpattern',help='Start of the match pattern')
parser.add_argument('-e', action='store', dest='endpattern',help='End of the match pattern')
parser.add_argument('-i', action='store', dest='ignorepattern',help='ignore lines with this')
parser.add_argument('-f', action='store', dest='infile',help='Input file name')
#parser.add_argument('f', type=argparse.FileType('r'))
args = parser.parse_args()

#print args.s

"""
if len(sys.argv) < 1:
        print "usage: provide a file to parse and filter " % (sys.argv[0])
        sys.exit(0)
print ("Args list : %s " %  sys.argv)
"""

infile = (args.infile)
#startpat = (sys.argv[2])
startpattern = re.compile(args.startpattern)
endpattern = re.compile(args.endpattern)
ignorepattern = re.compile(args.ignorepattern)

printdata = False
ignoreline = False


for line in fileinput.input(infile):
    if startpattern.search(line):
        printdata=True
    if ignorepattern.search(line):
        printdata=False
        ignoreline = True
    #only print stuff in the middle
    if printdata and len(line) >0:
        sys.stdout.write(line)
    #reset after the printline
    if ignoreline:
        ignoreline = False
    if endpattern.search(line):
        printdata = False


"""

nxml=lxml.objectify.parse(sys.argv[1])
nroot=nxml.getroot()
print("%s: %s"%(nroot.attrib.get("args"), nroot.attrib.get("startstr")))
#for nhost in nroot.findall("//*[local-name()='host']"):
for nhost in nroot.findall("//*[local-name()='host']"):
       for nname in nhost.hostnames:
              print('\t%s'%(nname.hostname.attrib.get("name")))
       for naddr in nhost.address:
              print('\t\t%s'%(naddr.attrib.get("addr")))
       for nport in nhost.ports.port:
              print('\t\t%s\t%s\t%s\t%s'%(nport.attrib.get("protocol"),
                                      nport.attrib.get("portid"),
                                      nport.state.attrib.get("state"),
                                      nport.service.attrib.get("name")
                                      ))
print(nroot.runstats.finished.attrib.get("summary"))
"""

"""
def convert(xml_file, xml_attribs=True):
    with open(xml_file, infile) as f:  # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)
"""
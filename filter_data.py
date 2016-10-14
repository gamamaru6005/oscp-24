#!/usr/bin/python
import sys
import fileinput
import json
import xmltodict
import lxml.objectify
import argparse
import re
import os
import fnmatch


parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
parser.add_argument('-s', action='store', dest='startpattern',help='Start of the match pattern',default='[a-zA-Z0-9]')
parser.add_argument('-e', action='store', dest='endpattern',help='End of the match pattern',default='^#StopAndIgnore')
parser.add_argument('-i', action='store', dest='ignorepattern',help='ignore lines with this',default='^#IgnoreThis')
parser.add_argument('-d', action='store', dest='indir',help='ignore lines with this',default='.\\')
parser.add_argument('-f', action='store', dest='infile',help='Input file name')
#args = parser.parse_args()
args, unknown = parser.parse_known_args()


infile = args.infile
indir = args.indir
sourcefiles = fnmatch.filter(os.listdir(indir),infile)
#print sourcefiles
"""
print "start pattern: " + args.startpattern
print "end pattern: " + args.endpattern
print "ignore pattern: " + args.ignorepattern
print "file name: " + args.infile
"""

startpattern = re.compile(args.startpattern)
endpattern = re.compile(args.endpattern)
ignorepattern = re.compile(args.ignorepattern)



for filelist in sourcefiles:
    printdata = False
    ignoreline = False
    #print "opening file named" + filelist
    for line in fileinput.input(indir + filelist):
        if ignorepattern.search(line) and printdata and (not startpattern.search(line)):
            printdata=False
            ignoreline = True
            #print "debug:ignore data is " + line
        if endpattern.search(line) and (not startpattern.search(line)):
            printdata = False
        if startpattern.search(line):
            printdata=True

    #only print stuff in the middle
        if printdata and len(line) >0:
            sys.stdout.write(line)
    #reset after the printline

            #print "debug: end pattern is " + line
        if ignoreline:
            ignoreline = False
            printdata = True




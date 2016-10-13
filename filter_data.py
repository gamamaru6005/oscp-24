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
args = parser.parse_args()


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



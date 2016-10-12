#!/usr/bin/python
import sys
import os
import nmap
from libnmap.parser import NmapParser

print "Starting nmap_to_xml"
if len(sys.argv) < 1:
        print "usage: provide a nmap xml file to convert to a csv " % (sys.argv[0])
        sys.exit(0)
print ("Args list : %s " %  sys.argv)
infile =(sys.argv[1])

#nm=nmap.PortScanner()

#with open(infile,"r") as fd:
#    content = fd.read()
#    nm.analyse_nmap_xml_scan(content)
#    print(nm.csv())

nmap_report = NmapParser.parse_fromfile(infile)
print "Nmap scan summary: {0}".format(nmap_report.summary)
print "####### banner "
print  sorted(set([ b.banner for a in nmap_report.hosts for b in a.services if 'product' in b.banner]))
print "####### open ports "
print  sorted(set([ b[0] for a in nmap_report.hosts for b in a.get_open_ports()]), key=int)
print "####### list nodes that have ports open"
print  [ a.address for a in nmap_report.hosts if (a.get_open_ports()) and 445 in [b[0] for b in a.get_open_ports()] ]
print "####### open ports listed by hosts"
print [ [a, [ b.address for b in nmap_report.hosts for c in b.get_open_ports() if a==c[0] ] ] for a in sorted(set([ b[0] for a in nmap_report.hosts for b in a.get_open_ports()]),key=int) ]

print "####### print ssl items "
print [ [a.address,  b.port] for a in nmap_report.hosts for b in a.services if b.tunnel=='ssl' or "'pem'" in str(b.scripts_results)  ]

print "####### print ssl/pem results"
print [ ':'.join([a.address,  str(b.port)]) for a in nmap_report.hosts for b in a.services if b.tunnel=='ssl' or "'pem'" in str(b.scripts_results)]
print "####### print new banners"
print [ [ a.address, b.port, b.servicefp ] for a in nmap_report.hosts for b in a.services if (b.service =='unknown' or b.servicefp) and b.port in [c[0] for c in a.get_open_ports()] ]

print "####### print services "
print sorted(set([ b.banner for a in nmap_report.hosts for b in a.services if 'product' in b.banner]))

print "####### print data"
print [ [ a, [ [b.address, c.port] for b in nmap_report.hosts for c in b.services if c.banner==a] ] for a in sorted(set([ b.banner for a in nmap_report.hosts for b in a.services if 'product' in b.banner])) ]
print "####### search by string"
# oracle used in this case
print [ [a.address, b.port] for a in nmap_report.hosts for b in a.services if b.open() and 'Oracle' in str(b.get_dict()) + str(b.scripts_results)]
print "############ urls listed"
urls = [ (b.service + b.tunnel).replace('sl','') + '://' + a.address + ':' + str(b.port) + '/' for a in nmap_report.hosts for b in a.services if b.open() and b.service.startswith('http') ]
for rawurls in urls:
    print rawurls
"""
for rawdata in nmap_report.get_raw_data():
    print rawdata
for scanned_hosts in nmap_report.hosts:
     print scanned_hosts
"""
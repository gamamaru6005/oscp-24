#!/usr/bin/env python

import time, sys
from pprint import pprint
from zapv2 import ZAPv2

# Here the target is defined and an instance of ZAP is created.
target = sys.argv[1]
#target = 'http://www.target.site/'
zap = ZAPv2()

# Use the line below if ZAP is not listening on 8090.

# ZAP starts accessing the target.
print 'Accessing target %s' % target
zap.urlopen(target)
time.sleep(2)

# The spider starts crawling the website for URLs
print 'Spidering target %s' % target
zap.spider.scan(target)

# Progress of spider
time.sleep(2)
print 'Status %s' % zap.spider.status
while (int(zap.spider.status) < 100):
   print 'Spider progress %: ' + zap.spider.status

   time.sleep(400)

print 'Spider completed'

# Give the passive scanner a chance to finish
time.sleep(5)

# The active scanning starts
print 'Scanning target %s' % target
zap.ascan.scan(target)
while (int(zap.ascan.status) < 100):
   print 'Scan progress %: ' + zap.ascan.status

   time.sleep(600)

print 'Scan completed'

# Report the results
print 'Hosts: ' + ', '.join(zap.core.hosts)
print 'Alerts: '
pprint(zap.core.alerts())

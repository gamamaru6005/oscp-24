#!/usr/bin/python
import requests
import re
from bs4 import BeautifulSoup
import sys

scripts = []
if len(sys.argv) != 2:
    print "usage: %s url" % (sys.argv[0])
    sys.exit(0)
tarurl = sys.argv[1]
url = requests.get(tarurl)
soup = BeautifulSoup(url.text,'lxml')

for line in soup.find_all('script'):
    newline = line.get('src')
    scripts.append(newline)
for script in scripts:
    if "jquery.min" in str(script).lower():
        url = requests.get(script)
        versions = re.findall(r'\d[0-9a-zA-Z._:-]+', url.text)
        if versions[0] == "2.1.1" or versions[0] == "1.12.1":
            print "Up to date"
        else:
            print "Out of date"
            print "Version detected: " + versions[0]
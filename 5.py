#!/usr/bin/env python

import pickle
import urllib2
from cStringIO import StringIO
import sys


url = "http://www.pythonchallenge.com/pc/def/peak.html"

response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
pdata = StringIO(response.read())
data = pickle.Unpickler(pdata).load()

for d in data:
    for line in d:
        sys.stdout.write(line[0] * line[1])
    sys.stdout.write("\n")

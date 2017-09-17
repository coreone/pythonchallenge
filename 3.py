#!/usr/bin/env python

import re

webpage = "http://www.pythonchallenge.com/pc/def/equality.html"

f = open("3.txt", "r")

found = []
for data in f:
    matches = re.findall(r"([^A-Z][A-Z]{3})([a-z]{1})([A-Z]{3}[^A-Z])", data)
    for m in matches:
        found.append(m[1])

print "".join(found)

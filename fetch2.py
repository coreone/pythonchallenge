#!/usr/bin/env python

import requests
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

response = requests.get(url)
lines = response.content.split("\n")

incomment = False
indata = False
numlines = 0
data = []
for line in lines:
    if re.search("^<\!\-\-", line):
        incomment = True
        numlines = 1
    elif re.search("^\-\->", line):
        incomment = False
        indata = False
        numlines = 0
    else:
        if indata:
            data.append(line)
        else:
            if incomment and numlines == 1:
                if re.search("^%%\$", line):
                    indata = True
                    data.append(line)
                    numlines += 1
                else:
                    numlines = 0

for d in data:
    if d:
        print d

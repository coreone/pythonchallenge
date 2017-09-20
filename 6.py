#!/usr/bin/env python

import re
import sys

url = "http://www.pythonchallenge.com/pc/def/channel.html"


def solution(directory=None):
    f = open("%s/readme.txt" % directory, "r")
    data = re.search(r"start from (\d+)", f.read())
    f.close()
    nothing = int(data.group(1))
    while True:
        f = open("%s/%d.txt" % (directory, nothing), "r")
        contents = f.read()
        data = re.search(r"Next nothing is (\d+)", contents)
        f.close()
        if data:
            nothing = int(data.group(1))
        else:
            return contents
            break


data = solution("6")

print data

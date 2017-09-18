#!/usr/bin/env python

import os

webpage = "http://www.pythonchallenge.com/pc/def/0.html"


def solution():
    return pow(2, 38)


result = solution()
base = os.path.dirname(webpage)
print "%s/%s.html" % (base, result)

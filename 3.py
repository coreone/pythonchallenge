#!/usr/bin/env python

import os
import re

webpage = "http://www.pythonchallenge.com/pc/def/equality.html"


def solution():
    f = open("3.txt", "r")

    found = []
    for data in f:
        matches = re.findall(
            r"([^A-Z][A-Z]{3})([a-z]{1})([A-Z]{3}[^A-Z])",
            data
        )
        for m in matches:
            found.append(m[1])

    return "".join(found)


result = solution()
base = os.path.dirname(webpage)
print "%s/%s.html" % (base, result)

#!/usr/bin/env python

import os
import sys

webpage = "http://www.pythonchallenge.com/pc/def/map.html"


def solution(s=None):
    theString = ""
    for i in s:
        n = ord(i)
        if n < 97 or n > 122:
            theString += i
        elif n >= 120:
            theString += chr(96 + (n-120))
        else:
            theString += chr(n+2)

    return theString


s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

result = solution(s)
print result

base = os.path.dirname(webpage)
nextpage = solution(os.path.basename(webpage).replace(".html", ""))
print "%s/%s.html" % (base, nextpage)

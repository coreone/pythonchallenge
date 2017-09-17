#!/usr/bin/env python

import sys

webpage = "http://www.pythonchallenge.com/pc/def/map.html"

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for i in s:
    n = ord(i)
    if n < 97 or n > 122:
        sys.stdout.write(i)
    elif n >= 120:
        sys.stdout.write(chr(96 + (n-120)))
    else:
        sys.stdout.write(chr(n+2))

sys.stdout.write("\n")

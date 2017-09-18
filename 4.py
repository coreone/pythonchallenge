#!/usr/bin/env python

import os
import re
import urllib2

webpage = "http://www.pythonchallenge.com/pc/def/linkedlist.php"


def solution(url=None):
    nothing = 12345
    while True:
        d = urllib2.urlopen("%s?nothing=%s" % (url, nothing))
        response = d.read()
        data = re.search("the next nothing is (\d+)", response)
        if data:
            nothing = int(data.group(1))
        else:
            if re.search("Yes. Divide by two and keep going.", response):
                nothing /= 2
            else:
                return response
                break


result = solution(webpage)
base = os.path.dirname(webpage)
print "%s/%s" % (base, result)

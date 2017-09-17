#!/usr/bin/env python

import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

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
            print response
            break

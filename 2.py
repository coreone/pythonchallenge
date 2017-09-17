#!/usr/bin/env python

webpage = "http://www.pythonchallenge.com/pc/def/ocr.html"

f = open("2.txt", "r")

chars = []
discard = []
for line in f:
    data = line.rstrip()
    for c in data:
        if c in chars:
            chars.remove(c)
        else:
            if c not in discard:
                discard.append(c)
                chars.append(c)

print ''.join(chars)

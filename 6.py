#!/usr/bin/env python

import os
import re
import requests
import zipfile

url = "http://www.pythonchallenge.com/pc/def/channel.html"


def prep(webpage=None, filename=None, directory=None):
    url = webpage.replace(".html", ".zip")
    # url = "http://www.pythonchallenge.com/pc/def/channel.zip"

    if webpage is None:
        raise Exception("No webpage given to prep function.")
    if filename is None:
        raise Exception("No filename given to prep function.")
    if directory is None:
        raise Exception("No directory given to prep function.")

    response = requests.get(url)

    out = open(filename, "w")
    out.write(response.content)
    out.close()

    if not os.path.isdir(directory):
        os.mkdir(directory)

    zip_ref = zipfile.ZipFile(filename, "r")
    zip_ref.extractall(directory)
    zip_ref.close()


def solution(filename=None, directory=None):
    result = ""

    if filename is None:
        raise Exception("No filename given to prep function.")
    if directory is None:
        raise Exception("No directory given to prep function.")

    f = open("%s/readme.txt" % directory, "r")
    zip_ref = zipfile.ZipFile(filename, "r")

    data = re.search(r"start from (\d+)", f.read())
    f.close()
    nothing = int(data.group(1))
    while True:
        result += zip_ref.getinfo("%d.txt" % nothing).comment
        f = open("%s/%d.txt" % (directory, nothing), "r")
        contents = f.read()
        data = re.search(r"Next nothing is (\d+)", contents)
        f.close()
        if data:
            result += zip_ref.getinfo("%d.txt" % nothing).comment
            nothing = int(data.group(1))
        else:
            print nothing
            print contents

            return result
            break

    zip_ref.close()


prep(url, "6.zip", "6")

print solution("6.zip", "6")

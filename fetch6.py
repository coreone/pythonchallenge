#!/usr/bin/env python

import os
import requests
import zipfile

url = "http://www.pythonchallenge.com/pc/def/channel.zip"

response = requests.get(url)

out = open("6.zip", "w")
out.write(response.content)
out.close()

if not os.path.isdir("6"):
    os.mkdir("6")

zip_ref = zipfile.ZipFile("6.zip", "r")
zip_ref.extractall("6")
zip_ref.close()

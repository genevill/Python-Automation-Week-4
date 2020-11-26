#! /usr/bin/env python3

import requests, glob, os

path = "supplier-data/images"
os.chdir(path)
pictures = []
pictures = glob.glob("*.jpeg")
url = "http://localhost/upload/"

for picture in pictures:
    with open(picture, "r") as opened:
        requests = requests.post(url, files={'file': opened})
        requests.raise_for_status()

#! /usr/bin/env python3

import os
import requests

path = "supplier-data/descriptions"
dirs = os.listdir(path)
files = []
for file in dirs:
    if file[-4:] == ".txt":
        files.append(file)
review = {}
os.chdir(path)
for file in files:
    f = open(file, "r")
    review["name"] = f.readline().rstrip('\n')
    review["weight"] = f.readline().rstrip('\n')
    review["description"] = f.readline().rstrip('\n')
    f.close()
print(review)
#response = requests.post("http://<corpweb-external-IP>/feedback", json=review)
#response.request.url
#response.request.body
#response.raise_for_status()

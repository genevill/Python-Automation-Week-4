#! /usr/bin/env python3

import os, requests, json

path = "supplier-data/descriptions"
dirs = os.listdir(path)
files = []
for file in dirs:
    if file[-4:] == ".txt":
        files.append(file)
fruit = {}
fruit_list = []
os.chdir(path)
for file in files:
    f = open(file, "r")
    fruit["name"] = f.readline().rstrip('\n')
    fruit["weight"] = int(f.readline().rstrip('\n').rstrip('lbs'))
    fruit["description"] = f.readline().rstrip('\n')
    f_name, ext = os.path.splitext(file)
    fruit["image_name"] = f_name + ".jpeg"
    fruit_list.append(fruit.copy())
    f.close()

for fruit in fruit_list:
    response = requests.post("http://[linux-instance-external-IP]/fruits", data=fruit)
    response.raise_for_status()

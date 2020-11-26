#!/usr/bin/env python3

#PIL library

#~/supplier-data/images

#change from 3000x2000 to 600x400

#change from .TIFF to .JPEG

from PIL import Image
import glob, os, sys

# go through a folder full of images and operate with each one
# wrong format, rotated 90 degrees, too large
# use PIL methods then write the new images in the right place

path = 'supplier-data/images'
os.chdir(path)

pictures = []
pictures = glob.glob("*.tiff")
#print(pictures)

for picture in pictures:
    f, e = os.path.splitext(picture)
    save = f + ".jpeg"
    if picture != save:
        try:
            with Image.open(picture) as im:
                im.convert("RGB").resize((600, 400)).save(save)
                print("Converting", picture)
        except OSError:
            print("cannot convert", picture)

#    print(save)

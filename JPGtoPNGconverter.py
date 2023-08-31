import os
import sys
from PIL import Image

file_path = sys.argv[1]
new_file_path = sys.argv[2]

isExist = os.path.exists(new_file_path)
directory = os.listdir(file_path)

if isExist:
    for files in directory:
        img = Image.open(file_path + "/" + files)
        img.save(new_file_path + "/" + files.split(".")[0] + ".png", 'png')
else:
    os.mkdir(new_file_path)
    for files in directory:
        img = Image.open(file_path + "/" + files)
        img.save(new_file_path + "/" + files.split(".")[0] + ".png", 'png')


# /Users/daniel/PycharmProjects/images/pokedex

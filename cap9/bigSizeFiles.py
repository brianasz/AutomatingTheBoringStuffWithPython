#!/bin/python3.6

import os, shutil

# Walk through a folder tree
for folder, subfolders, filenames in os.walk('/home/bsz/Fotos'):
  for filename in filenames:
    # Get files' sizes
    fileSize = os.path.getsize(folder + '/' + filename)
    # Identify files bigger than 100MG and print them
    if fileSize > 104857600:
      print(folder + '/' + filename + ': ' + str(fileSize) + ' bytes')

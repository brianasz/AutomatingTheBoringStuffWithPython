#!/bin/python3.6

import os, shutil

destination_path='/home/bsz/Python-Testing'
# Walk through a folder tree
for folder, subfolders, filenames in os.walk('/home/bsz/Python'):
  for filename in filenames:
    # Search for files with a certain extension
    if filename.endswith('.py'):
      # Copy the files into a new folder
      pyFiles = folder + '/' + filename
      shutil.copy(pyFiles, destination_path)
      print('File ' + folder + '/' + filename + ' copied over to ' + destination_path)

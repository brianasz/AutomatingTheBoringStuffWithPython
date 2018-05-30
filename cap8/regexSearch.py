#!/bin/python3.6

# Import all the modules
import os, re

# Get the user-supplied regular expression


# Identify the .txt files in the current directory
txtRegex = re.compile(r'\.txt$')
for filename in os.listdir(os.getcwd()):
  txtFound = txtRegex.search(filename)
  if txtFound != None:
    print(filename) 

# Search the user-supplied regular expression in all .txt files found in the directory

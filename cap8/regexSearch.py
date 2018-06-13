#!/bin/python3.6

# Import all the modules
import os, re

# Get the user-supplied regular expression
print("Enter the regular expression: ")
regEx = input()
regex = re.compile(regEx)
#regex = re.compile(r'(%s)'%regEx)

# Identify the .txt files in the current directory
txtRegex = re.compile(r'\.txt$')
for filename in os.listdir(os.getcwd()):
  txtFound = txtRegex.search(filename)
  if txtFound != None:
    print("File found: " + filename) 
  # Search the user-supplied regular expression in all .txt files found in the directory
    # Tasks: Open the file, get the text into a variable and check the regex against the variable containing the string.
    txtFile = open(filename)
    content = txtFile.read()
    txtFile.close()
    match = regex.search(content)
#    print(match.group())
    match = regex.findall(content)
    print(match)
  else:
    continue
# Note, the regex is not working fine yet. Improve this. 

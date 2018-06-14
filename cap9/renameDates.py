#!/bin/python3.6

# README section
'''
renameDates.py:

1) It searches all the filenames in the current working directory for American-style dates.

2) When one is found, it renames the file with the month and day swapped to make it European-style.
'''

import shutil, os, re
# Create a regex for american style dates
datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""",re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
  mo = datePattern.search(amerFilename)
  # Skip files without a date.
  if mo == None:
    continue
  # Get the different parts of the filename. 
  beforePart = mo.group(1)
  monthPart  = mo.group(2)
  dayPart    = mo.group(4)
  yearPart   = mo.group(6)
  afterPart  = mo.group(8)
# Form the European-style filename. 
  euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# Get the full, absolute file paths. 
  absWorkingDir = os.path.abspath('.')
  amerFilename = os.path.join(absWorkingDir, amerFilename)
  euroFilename = os.path.join(absWorkingDir, euroFilename)
# Rename the files. 
  print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
  #shutil.move(amerFilename, euroFilename

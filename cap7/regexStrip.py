#!/usr/bin/python3.6

import sys, re

def regexStrip(theList):
  if (len(theList)) == 2:
    string = theList[0]
    pattern = theList[1]
    myregex = re.escape(pattern) + r"+"
    result = re.search(myregex, string, re.IGNORECASE)
    print(re.sub(myregex, '', string))
  else:
    print(re.sub('^\s+|\s+$', '', theList)) 

myList1 = '       This is the string with space characters....wow!!!       '
myList2 = ['000000This is the string with zeros on it....wow!!!0000000', '0']
regexStrip(myList1)
regexStrip(myList2)

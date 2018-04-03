#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import sys

#print(len(sys.argv))

def regexStrip(theList):
  if (len(theList)) == 2:
    string = theList[0]
    pattern = theList[1]
    stripRegex = re.compile(r'^%s' % pattern)
    stripRegex.search(string)
    print(string)
    print(pattern)


myList = ['0000000this is string example....wow!!!0000000', '0']
regexStrip(myList)

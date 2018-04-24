#!/bin/python3.6

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
  mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
  mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delall':
  mcbShelf.clear()
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
  elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

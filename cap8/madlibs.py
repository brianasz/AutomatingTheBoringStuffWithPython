#!/bin/python3.6

import re

f = open('./madlibs.txt').read()
for word in f.split():
  if "ADJECTIVE" in word:
    print("Enter a new adjective: ")
    newAdj = input()
    f = f.replace("ADJECTIVE", newAdj)
  if "NOUN" in word:
    print("Enter a new noun: ")
    newNoun = input()
    f =  f.replace("NOUN", newNoun, 1)
  if "VERB" in word:
    print("Enter a new verb: ")
    newVerb = input()
    f =  f.replace("VERB", newVerb)

fileObj = open('./madlibs.txt', 'w')
fileObj.write(f)
fileObj.close()

fileObj = open('./madlibs.txt')
fileContent = fileObj.read()
print(fileContent)

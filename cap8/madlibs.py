#!/bin/python3.6

fileObj = open('./madlibs.txt')
fileContent = fileObj.read()
fileObj.close()

for word in fileContent.split():
  print(word)
"""  if word == "ADJECTIVE":
    print('Enter an adjective: ')
    newWord = input()
    fileObj = open('./madlibs.txt')
    fileContent = fileObj.read()
    fileObj.close()
    replacement = fileContent.replace("ADJECTIVE", newWord)  
    fileObj = open('./madlibs.txt', 'w')
    fileObj.write(replacement)
    fileObj.close()
  elif word == "NOUN":
    print('Enter a noun: ')
    newWord = input()
    fileObj = open('./madlibs.txt')
    fileContent = fileObj.read()
    fileObj.close()
    replacement = fileContent.replace("NOUN", newWord)
    fileObj = open('./madlibs.txt', 'w')
    fileObj.write(replacement)
    fileObj.close()
  elif word == "VERB":
    print('Enter a verb: ')
    newWord = input()
    fileObj = open('./madlibs.txt')
    fileContent = fileObj.read()
    fileObj.close()
    replacement = fileContent.replace("VERB", newWord)
    fileObj = open('./madlibs.txt', 'w')
    fileObj.write(replacement)
    fileObj.close()
"""
fileObj = open('./madlibs.txt')
fileContent = fileObj.read()
print(fileContent)

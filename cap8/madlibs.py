#!/bin/python3.6

import re

f = open('./madlibs.txt').read()
#fileContent = fileObj.read()

for word in f.split():
  if word == 'ADJECTIVE':
#  if 'ADJECTIVE' in open('./madlibs.txt').read():
    print("Enter a new adjective: ")
    newAdj = input()
    fileObj = open('./madlibs.txt', 'r')
    fileContent = fileObj.read()
    fileObj.close()

    newData = fileContent.replace('ADJECTIVE', newAdj)

    fileObj = open('./madlibs.txt', 'w')
    fileObj.write(newData)
    fileObj.close()
  if word == 'NOUN':
#  if 'NOUN' in open('./madlibs.txt').read():
    print("Enter a new noun: ")
    newNoun = input()
    fileObj = open('./madlibs.txt', 'r')
    fileContent = fileObj.read()
    fileObj.close()

    newData = fileContent.replace('NOUN', newNoun)

    fileObj = open('./madlibs.txt', 'w')
    fileObj.write(newData)
    fileObj.close()
  if word == 'VERB':
#  if 'VERB' in open('./madlibs.txt').read():
    print("Enter a new verb: ")
    newVerb = input()
    fileObj = open('./madlibs.txt', 'r')
    fileContent = fileObj.read()
    fileObj.close()

    newData = fileContent.replace('VERB', newVerb)

    fileObj = open('./madlibs.txt', 'w')
    fileObj.write(newData)
    fileObj.close()




'''
adjRegex = re.compile(r'ADJECTIVE')
if adjRegex.search(fileContent).group() != None:
  print('A Match')

adjRegex = re.compile(r'ADJECTIVE')
adjMatch = adjRegex.search(fileContent).group()
print(adjMatch)

nounRegex = re.compile(r'NOUN')
nounMatch = nounRegex.search(fileContent).group()
print(nounMatch)

verbRegex = re.compile(r'VERB*')
verbMatch = verbRegex.search(fileContent).group()
print(verbMatch)


adjMatch.sub(




for word in fileContent.split():
  if word == adjMatch:
    print('There is an ADJECTIVE')
  if word == nounMatch:
    print('There is a NOUN')
  if word == 'VERB.':
    print('There is a VERB')

  print('Please enter an adjective')
  adjInput = input()
  print(adjInput)

adjRegex = re.compile(r'ADJECTIVE')
adjRegex.sub(adjInput, 

for word in fileContent.split():
  print(word)
  if word == "ADJECTIVE":
    print('Enter an adjective: ')
    newWord = input()
    print(newWord)
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
'''
fileObj = open('./madlibs.txt')
fileContent = fileObj.read()
print(fileContent)

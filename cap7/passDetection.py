#!/bin/python3.6

import re

while True: 
  def passRegex(password):
    # Check it is 8 characters lenght
    checkLenght = re.compile(r'[a-zA-Z0-9]{8,}')
    foundLenght = checkLenght.search(password)
    # Check it contains at least one digit number
    checkDigit = re.compile(r'\d+')
    foundDigit = checkDigit.search(password)
    # Check it contains lowercase letters
    checkUpper = re.compile(r'[A-Z]+')
    foundUpper = checkUpper.search(password)
    # Check it contains uppercase letters    
    checkLower = re.compile(r'[a-z]+')
    foundLower = checkLower.search(password)

    if foundLenght != None and foundDigit != None and foundUpper != None and foundLower != None:
      return True
    elif foundLenght == None or foundDigit == None or foundUpper == None or foundLower == None:
      if foundLenght == None:
        print("Error: Your password must be at least 8 characters long")
      if foundDigit == None:
        print("Error: Your password must have at least 1 digit number")
      if foundUpper == None:
        print("Error: Your password must have at least one uppercase character")
      if foundLower == None:
        print("Error: Your password must have at least one lowercase character")
      return False

  print("Please enter a password: ")
  userPassword = input()
  if passRegex(userPassword) == True:
    print("Password succesfully submitted")
    break
  else:
    print("Please try another password...")
    continue

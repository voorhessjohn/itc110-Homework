import os
import re


rawRegex = input('enter a regular expression:')
re.compile(rawRegex)
    

userRegex = re.compile(rawRegex)
for file in os.listdir(os.getcwd()): #I figured it would be easier to run this in the current working directory than having the user supply the directory.
    if file.endswith(".txt"):#ghostdog74 on StackOverflow for 'endswith'
        print(file)
        fileOpen = open(file)
        fileContent = fileOpen.read()
        mo = userRegex.search(fileContent)
        if mo is None:#Ian McMahon on StackOverflow for exception handling
           print('None') 
        else:
            print(mo.group())

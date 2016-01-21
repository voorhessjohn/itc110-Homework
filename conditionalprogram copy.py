Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print('Hello world')
print('What is your name?')
myName = input()
if myName == 'Kid Rock':
  print('That is not funny')
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = int(input())
if myAge > 40:
  print('You were born before the 80s')
elif myAge < 40:
  print('You will be ' + str(int(myAge) + 1) + ' in a year.')

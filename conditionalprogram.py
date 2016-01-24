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

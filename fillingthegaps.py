import os

os.chdir('/')
i = 1
path = 'Users/johnglennvoorhess/delicious'
for filename in os.listdir('Users/johnglennvoorhess/delicious'):
    if filename.endswith(".txt") and filename.startswith('spam'):
        print(filename)
        os.rename(str(path)+'/'+str(filename), str(path)+'/spam'+str(i)+'.txt')
        i += 1
        #This is my 'brute force' solution.
        #Instead of finding gaps and rearranging things
        #like a fancy program, it says 'your filename sequence is broken - here's
        # a better one.' It can be adapted to add leading '00's if desired.    

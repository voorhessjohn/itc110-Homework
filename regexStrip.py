import re                                           #imports regular expressions
def regexStrip(string, chars='\s'):                 #function regexStrip is defined as the string to be stripped and the characters to be stripped from it
    if chars != '\s':                               #if chars entered by user do not equal a space,
        chars = '[' + chars + ']'                   #then chars equals [chars]
    regexFormat = '^' + chars + '*|' + chars + '*$' #The regex begins with [chars] that appear one or more times (*) OR (|) ends with ($) characters one or more times (*). This line establishes the format for the regular expression that defines the function
    stripRegex = re.compile(regexFormat)            #stores the regular expression defined above as the variable strippedString          
    strippedString = stripRegex.sub('', string)     #stores the substituted nothing ('') for string in the variable strippedString
    print(strippedString)
    return strippedString
testString = input()
regexStrip(testString)
# I had a hard time getting this one started.  I commented Joseph Wanderer's code to get a feel for how his version works.
# I am still not 100% clear on this, so I am asking him to break it down line by line for me before class.
# Below are the credits that he gave.

# Credit to Synes_Godt_Om on the reddit forum below. The pipe was the key.
# https://www.reddit.com/r/inventwithpython/comments/3m3m3w/regex_version_of_strip_from_automate_the_boring/

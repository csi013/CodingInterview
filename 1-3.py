#URLify 2017 09 05 CSI#
#Python#

def ReplaceWhiteSpace(inputString):
    wordList = inputString.split()
    answer = "%20".join(wordList)
    print(answer)
    
string = input('string:')

ReplaceWhiteSpace(string)


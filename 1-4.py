#Palindrome Permutation 2017 09 05 CSI#
#Python#

def CheckPelindromePermutation(inputString):
    checkFlag = 0
    for c in inputString:
        if(inputString.count(c) % 2 != 0):
            if(checkFlag == 0):
                checkFlag+=1
                continue
            else:
                return False
    return True

print(CheckPelindromePermutation(input("Input string:")))rint('True')


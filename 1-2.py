#check Permutation 2017 09 04 CSI#

def CheckPermutation(Str1,Str2):
    if len(Str1) == len(Str2):
        Str1 = sorted(Str1)
        Str2 = sorted(Str2)
        if Str1 == Str2:
            print('True')
        else:
            print('False')
    else:
        print('False')

Str1 = input("string1: ")
Str2 = input("string2: ")
CheckPermutation(Str1,Str2)

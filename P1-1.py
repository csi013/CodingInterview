#CSI
#Time Complexity : O(n^2)
#Space Complexity : O(n)

#Check unique character
def checkString(stringInput):
		checkBit=0
		for c in stringInput:
			if stringInput.count(c) > 1:
				checkBit = 1
				return checkBit
			else:
			 	checkBit = 0
		return checkBit

#Main section
stringInput = input("input string :")
if checkString(stringInput) == 1:
	print("False")
else:
	print("Pass")


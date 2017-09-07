#String Compression 2017 09 05 CSI#
#Python#
def StringCompression(String):
    tmp = String[0]
    resultString = ""
    count = 1
    for i in range(1,len(String)):
        if(i == len(String)-1):
            count+=1
            resultString += tmp + str(count)
            continue
        if(tmp == String[i]):
            count+=1
        else:
            resultString += tmp + str(count)
            count=1
        tmp = String[i]        
    return resultString
inputString = input("input string:")
print(StringCompression(inputString))


#is Unique 2017 09 03 CSI#

Str = input('Input String : ')
flag = 0;
for c in Str:
    if Str.count(c) != 1:
        flag = 1
        break
if flag == 1:
    print('False')
else:
    print('True')

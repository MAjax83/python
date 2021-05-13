userStr = input("введите строку с пробелами ")
dataStr = []
i = 0
dataStr = userStr.split()
countDataStr = dataStr.__len__()
#for data in range(userStr.count(' ') + 1):
#for data in countDataStr:
while i < countDataStr:
    if len(str(dataStr[i])) <= 10:
        print(f" {i+1} {dataStr [i]}")
        i += 1
    else:
        print(f" {i+1} {dataStr [i] [0:10]}")
        i += 1
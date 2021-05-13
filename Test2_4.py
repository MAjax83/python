userStr = input("введите строку с пробелами ")
dataStr = []
i = 1
for data in range(userStr.count(' ') + 1):
    dataStr = userStr.split()
    if len(str(dataStr)) <= 10:
        print(f" {i} {dataStr [data]}")
        i += 1
    else:
        print(f" {i} {dataStr [data] [0:10]}")
        i += 1
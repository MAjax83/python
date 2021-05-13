countList = int(input("Введите количество элементов в списке "))
userList = []
it = 0
iterator = 0
while it < countList:
    userList.append(input("Добавить новое значение в список "))
    it += 1

for data in range(int(len(userList)/2)):
        userList[iterator], userList[iterator + 1] = userList [iterator + 1], userList[iterator]
        iterator += 2
print(userList)
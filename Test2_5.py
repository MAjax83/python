userList = [7, 5, 3, 3, 2]

while True:
    key = input("Введите число или нажмите 'Q' для выхода ").upper()
    if key == 'Q':
        break
    userValue = int(key);

    for data in range(len(userList)):
        if userList[data] == userValue:
            userList.insert(data + 1, userValue)
            break
        elif userList[-1] > userValue:
            userList.append(userValue)
        elif userList[0] < userValue:
            userList.insert(0, userValue)
        elif userList[data] > userValue \
                and userList[data + 1] < userValue:
            userList.insert(data + 1, userValue)

    print(f"Итоговый список - {userList}")

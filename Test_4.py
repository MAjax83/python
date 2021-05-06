count = input('введите число для расчета: ')
countInt = int(count)
temp = -1
while countInt > 10:
    newCount = countInt % 10
    countInt //= 10
    if newCount > temp:
        temp = newCount
print('Самое большая цифра = ', temp)

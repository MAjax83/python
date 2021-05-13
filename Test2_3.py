dictSeason = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
listSeason = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input("Введите номер месяца от 1 до 12"))
if month == 12 or month == 1 or month == 2:
        print(dictSeason.get(1))
        print(listSeason[0])
elif month == 3 or month == 4 or month ==5:
    print(dictSeason.get(2))
    print(listSeason[1])
elif month == 6 or month == 7 or month == 8:
    print(dictSeason.get(3))
    print(listSeason[2])

elif month == 9 or month == 10 or month == 11:
    print(dictSeason.get(4))
    print(listSeason[3])
else:
        print("Значение не входит в диапозон ")
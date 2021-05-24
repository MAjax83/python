def summa():
    try:
        with open('Test_5_5.txt', 'w+') as my_file:
            line = input('Введите цифры через пробел \n')
            my_file.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильный ввод. Ошибка!')
summa()
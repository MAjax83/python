def div(*args):

    try:
        d1 = int(input("Введите делимое "))
        d2 = int(input("Введите делитель "))
        dd = d1 / d2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return "Деление на 0 запрещено!"

    return dd


print(f'result  {div()}')
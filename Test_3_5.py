def calc_sum ():
    result = 0
    ex = False
    while ex == False:
        line_number = input('Введите последовательность чисел или Q для заверщения - ').split()

        res = 0
        for el in range(len(line_number)):
            if line_number[el] == 'q' or line_number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(line_number[el])
        result = result + res
        print(f'сумма введенной последовательности {result}')
    print(f'Окончательная сумма {result}')


calc_sum()
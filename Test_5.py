profit = int(input('введите прибыль: '))
loss= int(input('введите издержки: '))

if profit > loss:
    print('отработали с прибылью ', profit/loss*100, '%')
    numb = int(input('введи число сотрудников: '))
    print('выручка на каждого сотрудника составила ', profit/numb)
else:
    print('отработали с убытком!' )




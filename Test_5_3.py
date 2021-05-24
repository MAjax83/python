with open('Test_5_3.txt', 'r',1,"UTF") as my_file:
    sal = []
    FIO = []
#    my_list = my_file.read().split('\n')
    for line in my_file:
        str = line.split()
        if int(str[1]) < 20000:
           FIO.append(str[0])
        sal.append(str[1])
print(f'Оклад меньше 20.000 {FIO}, средний оклад {sum(map(int, sal)) / len(sal)}')
rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('Test_5_4.txt', 'r',1,"UTF") as my_file:
    #content = file_obj.read().split('\n')
    for line in my_file:
        str = line.split(' ', 1)
        new_file.append(rus[str[0]] + '  ' + str[1])
    print(new_file)

with open('Test_5_4_new.txt', 'w',1,"UTF") as my_file_2:
    my_file_2.writelines(new_file)

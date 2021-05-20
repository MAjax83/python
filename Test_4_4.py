list = [7, 5, 5, 9, 4, 7, 7, 10, 8, 8]
new_list = [el for el in list if list.count(el) == 1]
print(new_list)
my_list = [6, 1, 4, 19, 71, 9, 12, 3, 1]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)
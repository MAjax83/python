def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_func = []
for el in fibo_gen(7):
    if i > 15:
        break
    else:
        my_func.append(el)
        i += 1
print(my_func)
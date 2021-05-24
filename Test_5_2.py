with open("Test_5_2.txt","r",1,"UTF") as my_file:
    letters = 0
    i = 0

    for line in my_file:
        i = i + 1
        print(f" символов в строке {len(line)}")
    print(f"Строк всего {i}")



subj = {}
with open('Test_5_6.txt', 'r',1,'UTF') as my_file:
    for line in my_file:
        str = line.replace('(', ' ').split()
        subj[str[0][:-1]] = sum(int(i) for i in str if i.isdigit())

        #subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету - \n {subj}')
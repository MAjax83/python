import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('Test_5_7.txt', 'r',1, "UTF") as file:
    for line in file:
        #name, firm, earning, damage = line.split()
        str = line.split()
        profit[str[0]] = int(str[2]) - int(str[3])
        if profit.setdefault(str[0]) >= 0:
            prof = prof + profit.setdefault(str[0])
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'average_profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('Test_5_7.json', 'w') as file_js:
    json.dump(profit, file_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
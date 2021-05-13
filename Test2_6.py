tupleList = []
i = 1
while True:
    tupleList.append(
        (input('Введите номер товара: '), dict({
            'название': str(input('Введите название: ')),
            'eдиница': str(input('Введите единцу измерения: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
        }))
    )

    if input('Добавить еще товар? (Y/N): ').upper() == 'N':
        break
    i += 1

print(f'Список товаров:{tupleList}')

dictData = dict({})
for product in tupleList:
    for key, value in product[-1].items():
        if key in dictData:
            if value not in dictData.get(key):
                dictData.get(key).append(value)
        else:
            dictData.update({key: [value]})


print(f'аналитика: {dictData}')

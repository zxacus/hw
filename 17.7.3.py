per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вклада: '))
deposit = list(int(i * money / 100) for i in list(per_cent.values()))
print(deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))

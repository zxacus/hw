tickets = int(input('При заказе от 4 билетов скидка 10%\nВведите количество билетов: '))
if not tickets:
    print('Ждём вас снова')
    quit()
if tickets < 0:
    tickets = int(input('Количество билетов не может быть отрицательным\nВведите количество билетов: '))

clients_age = [int(input(f'Введите возраст {i + 1} посетителя: ')) for i in range(tickets)]
while any(val < 0 or val > 144 for val in clients_age):
    print('Возраст посетителей не может быть меньше 0 и больше 144 лет')
    clients_age = [int(input(f'Введите возраст {i + 1} посетителя: ')) for i in range(tickets)]

sum = 0

for age in clients_age:
    if 0 <= age < 18:
        pass
    if 18 <= age < 25:
        sum += 990
    if 25 <= age <= 144:
        sum += 1390

if tickets <= 3:
    print(f'Сумма к оплате: {sum} руб.')
if tickets > 3:
    print(f'Сумма к оплате c учётом скидки 10%: {sum * 0.9} руб.')

'''
Выручка и издержки фирмы
'''

profit = int(input('Введите выручку своей фирмы '))
costs = int(input('Введите издержки свой фирмы '))
result = profit - costs
rel_profit = 0
rentability = profit / costs
qty = 0

if result > 0:
    print('Ваша фирма работает с прибылью: ' + str(result) + ' р.')
    print('Рентабельность вашей фирмы: ' + ("%.2f" % rentability))
    qty = int(input('Введите кол-во сотрудников вашей фирмы  '))
    rel_profit = result / qty
    print('Прибыль в рассчете на одного сотрудника = ' + str(rel_profit) + ' p.')
else:
    print('У вас нет прибыли, однако!')

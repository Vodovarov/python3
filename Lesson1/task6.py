'''
Спортсмен и его ежедневные пробежки
'''

a = int(input('Сколько км спортсмен пробежал в 1-й день? Введите число '))
b = int(input('Введите желаемый результат пробега в день, км: '))
day = 1

while a < b:
    a = a + a * 0.1
    day += 1

print('Спортсмену понадобилось ' + str(day) + ' дней, \nчтобы увеличить пробег до ' + str(b) + ' км в день')

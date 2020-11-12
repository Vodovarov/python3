"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
import sys
import os

try:
    f = open('task5.3.txt', 'r', encoding='utf-8')
    print('Зарплата меньше 20000р:\n')
    i = 0
    salary = 0

    for line in f:
        a = line.split()
        i += 1
        salary += int(a[1])
        if int(a[1]) < 20000:
            print(f'Сотрудник: {a[0]}')

    print(f'\nСредняя зп по фирме = {salary/i}')
    f.close()

except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))

"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(*args):
    try:
        a = int(input('Введи первый аргумент '))
        b = int(input('Введи второй аргумент '))
        c = int(input('Введи третий аргумент '))

        if a >= b:
            if b >= c:
                return a + b
            else:
                return a + c
        elif a <= b:
            if a <= c:
                return b + c
            else:
                return a + b
        else:
            return b + c
    except ValueError:
        return 'Value error'


print(str(my_func(2, 4, 6)))

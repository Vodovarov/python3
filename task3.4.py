"""
4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись
без встроенной функции возведения числа в степень.
"""


def my_func(x:float, y:int):
    try:
        res = x ** (1*y)
        #res = 1 / x ** abs(y)
        return res
    except TypeError:
        return 'Type error'


def my_func2(x:float, y:int):
    try:
        res = x * y
        return res
    except TypeError:
        return 'Type error'


print(my_func(2, -2))

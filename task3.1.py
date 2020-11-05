"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление.
 Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
"""
def my_division(*args):

    try:
        num1 = float(input("Введи делимое... "))
        num2 = float(input("введи делитель...  "))
        result = num1 / num2
    # обработка деления на 0:
    except ZeroDivisionError:
        return "Деление на 0!"
    # обработка введенных значений:
    except ValueError:
        return 'Value error'

    return round(result, 3)


print('Результат: ' + str(my_division()))




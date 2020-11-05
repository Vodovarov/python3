"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""


def my_sum():
    try:
        fin_sum = 0
        flag = False

        while flag == 0:
            number = input('Введите числа через пробел. Нажмите Q для выхода... ').split()
            res = 0
            for elem in range(len(number)):
                if number[elem].lower() == 'q':
                    flag = True
                    break
                else:
                    res = res + int(number[elem])
            fin_sum = fin_sum + res
            print('Сумма введенных чисел = ' + str(fin_sum))

    except ValueError:
        return print('Value error')

    print('Общая сумма = ' + str(fin_sum))


my_sum()
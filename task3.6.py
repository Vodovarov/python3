"""
Реализовать функцию int_func(), принимающую слово
из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(x:str):
    upper = x[:1].upper()
    return upper + x[1:]


def my_map(func, iter_object):
    res = []
    for word in iter_object.split():
        res.append(func(word))
    return res


print(my_map(int_func, 'the dire straits english band'))
print(my_map(int_func, str(input('Введите несколько слов строчными латинскими буквами через пробел...'))))
# print(int_func('uiong'))

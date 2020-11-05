"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def long_string_func(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(long_string_func(name='Andrey', surname='Woo', year='1980', city='SPb', email='vodo5000@mail.ru', phone='+7(921)5556551'))

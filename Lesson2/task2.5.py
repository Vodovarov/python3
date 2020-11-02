"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
my_list = [31, 11, 8, 8, 6]
print('Есть набор натуральных чисел' + str(my_list))
new_elem = int(input('Введите новый элемент-число\n'))
new_elem_count = my_list.count(new_elem)
# print(new_elem_count)

if not new_elem_count:

    if new_elem < my_list[-1]:
        my_list.append(new_elem)
    else:
        for idx, item in enumerate(my_list):
            if item < new_elem:
                my_list.insert(idx, new_elem)
                break
else:
    end_index = my_list.index(new_elem) + new_elem_count
    my_list.insert(end_index, new_elem)

print(my_list)

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

try:
    # f = open('task5.4.txt', 'r', encoding='utf-8')
    with open('task5.4.txt', 'r', encoding='utf-8') as f1, open('task5.4-bis.txt', 'w', encoding='utf-8') as f2:
        a = []
        for line in f1:
            a = line.split()
            for key in my_list:
                if a[0] == key:
                    a[0] = my_list[key]
                    for el in a:
                        f2.write(el + ' ')
                        if el.isdigit():
                            f2.write('\n')
except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))





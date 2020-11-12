"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

try:
    f = open('task5.2.txt', 'r', encoding='utf-8')
    i = 0
    qty = 0
    result = {}
    for line in f:
        i += 1
        qty = len(line.split())
        result.setdefault(i, qty)

    print('Всего строк в файле: ' + str(i))
    print('Слов построчно: ')
    for key, value in result.items():
        if key == 2:
            print(f'Вo {key}-й строке: {value} слов')
        else:
            print(f'В {key}-й строке:  {value} слов')

    f.close()

except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))

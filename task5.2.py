"""
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

try:
    f = open('task5.2.txt', 'r')
    i = 0
    qty = 0
    result = {}
    for line in f:
        i += 1
        qty = len(line.split())
        result.setdefault(i, qty)

    print('Всего строк в файле: ' + str(i))
    for key, value in result.items():
        print(f'В {key}-й строке:  {value} слов')

except IOError as e:
    print('I/O error({0}): {1}'.format(e.errno, e.strerror))

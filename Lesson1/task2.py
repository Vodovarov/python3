'''
divmod(a, b) - возвращает пару частное-остаток от деления аргументов
'''

seconds = int(input('INPUT SECONDS YOU WANT TO TRANSFORM\n'))

m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))


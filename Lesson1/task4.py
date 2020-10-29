'''
Find the max digit in user number
'''

user_number = int(input('Введите число, да лучше многоразрядное :) \n'))
max_number = 0
while user_number > 0:
    if max_number < user_number % 10:
        max_number = user_number % 10
    user_number = user_number // 10

print(max_number)
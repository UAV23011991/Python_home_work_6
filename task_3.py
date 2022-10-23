# home_work_3
# task_2

# Напишите программу, которая найдёт произведение пар чисел списка 
# (Список создаем как в предыдущем задании). Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.

# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# number = int(input('Введите размер списка: '))
# list = []
# list2 = []

# for i in range(number):
     # list_number = int(input(f'Введите число {i+1}: '))
     # list.append(list_number)

# for i in range(len(list)):
    # while i < len(list)/2 and number > len(list)/2:
        # number = number - 1
        # a = list[i] * list[number]
        # list2.append(a)
        # i += 1

# print(f'Заданный пользователем список: {list}.')
# print(f'Ответ:{list2}.')

import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print(f'Заданный пользователем список: {list_a}.')          # при желании данную строку можно закомментировать сути это не изменит
print(f'Ответ: {list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])])}.')

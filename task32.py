# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random 
list = [random.randint(-10, 20) for i in range(12)]
number_one = int(input('Введите минимальное число диапазона поика: '))
number_two = int(input('Введите максимальное число диапазона поика: '))
print(list)

for i in range(len(list)):
    if number_one <= list[i] <= number_two:
        print(i, end = ' ')
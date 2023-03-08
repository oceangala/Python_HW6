# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
sp_start = [random.randint(0, 100) for i in range(20)]
# print(sp_start)

left_n, right_n = int(input()), int(input())
print([i for i in range(len(sp_start)) if left_n <= sp_start[i] <= right_n])
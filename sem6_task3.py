# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3
# Вывод:
# 2

import random

n = int(input('Введите длину списка '))

sp = [random.randint(0, 10) for i in range(n)]
print(sp)
counter = 0
cntrl = []
for i in range(n):
    if sp.count(sp[i])>=2 and sp[i] not in cntrl:
        counter += sp.count(sp[i])//2
        cntrl.append(sp[i])
              
print(counter)
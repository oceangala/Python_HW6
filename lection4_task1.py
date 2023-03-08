# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# import random
# sp = [random.randint(1, 12) for i in range(12)]
# print(sp)
# res = []
# for i in sp:
#     if i%2 == 0:
#         res.append((i, i**2))

# print(res)


import random
sp = [random.randint(1, 12) for i in range(12)]
print(sp)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

res = select(str, sp)
print(res)

res = select(int, res)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res)

res = select(lambda x: (x, x**2), res)
print(res)
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Диапазон от 6 до 12
# Вывод: [1, 9, 13, 14, 19]


import random
n = abs(int(input('Введите количество элементов массива: ')))
numA = abs(int(input('Введите начало диапазона (от): ')))
numB = abs(int(input('Введите конец диапазона (до): ')))
col = []
for i in range(n):
    col.append(random.randint(-10, 11))

print(col)

def IndexAr(a, b, arr, indar=[]):
    for i in range(len(arr)):
        if arr[i]>=a and arr[i]<=b:
            indar.append(i)
    return indar
print(f'Индексы элементов в диапазоне от {numA} до {numB}')
print(IndexAr(numA, numB, col))
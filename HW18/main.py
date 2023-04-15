# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random
n = int(input('Введите количество чисел в массиве А[1..N]: '))
col = []
for i in range(n):
    col.append(random.randint(1, 10))
print(col)
col = list(set(col))
col.sort()
print(col)
x = int(input('Введите число X для поиска ближайшего в массиве A[1..N]: '))
flag = False
j=0
temp=0
min = col[0]
if x<col[0]:
    temp=0
else:
    while flag==False:
        if col[j]>x:
            temp=j-1
            flag=True
        else:
            flag=False
        j=j+1
print(col[temp])

        

    
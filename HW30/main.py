# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

numA1 = abs(int(input('Введите первый элемент прогрессии А1: ')))
numD = abs(int(input('Введите разность прогрессии d: ')))
numN = abs(int(input('Введите количество элементов прогрессии N: ')))

# def ArElment (a, d, n): # через цикл
#     col=[]
#     for i in range(n):
#         col.append(a+d*i)
#     return col
# print(ArElment(numA1, numD, numN))

def ArElment (a, d, n, i=0, col=[]): # через рекурсию (в качестве тренировки)
    if i<n:
        col.append(a+d*(i))
        ArElment(a, d, n, i+1)
    return col
print(ArElment(numA1, numD, numN))
# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

numA = abs(int(input('Введите число А: ')))
numB = abs(int(input('Введите число B: ')))
def expon (x, n):
    if n==0:
        return 1
    if n>0:
        temp = expon(x, n-1) *x
    return temp

print(expon(numA, numB))
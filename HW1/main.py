# Задача 2: Найдите сумму цифр трехзначного числа

print("Введите трехзначное число: ")
number = int(input())
flag = False
while flag == False:
    if (number > 999 or number < 100):
        print("введено некорректное число, введите еще раз трехзначное число: ")
        number = int(input())
        flag = False
    else:    flag = True
size = 3
i = 0
temp = 0
summ = 0
while i<size:
    temp = number % 10
    summ = summ + temp
    number = number//10
    i=i+1

print(f"сумма цирф равна: {summ}")

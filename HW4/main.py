# Задача 8: Требуется определить, можно ли от шоколадки размером n x m долек
# отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
print('введите число n: ')
n = int(input())
print('введите число m: ')
m = int(input())
print('введите число k: ')
k = int(input())
print(f"имеем шоколадную плитку размером {n} x {m} с чилом плиток", n*m)
temp = 0
i=1
j=1
size1 = n-1
size2 = m-1
fl1=False
fl2=False
while i<=size1:
    temp = m*i
    if k==temp:
        fl1=True
    i=i+1
while j<=size2:
    temp = n*j
    if k==temp:
        fl2=True
    j=j+1
if fl1==True or fl2==True:
    print(f"От шоколадки можно отломать {k} плиток один раз")
else: print("Отломать правильный кусок невозможно")
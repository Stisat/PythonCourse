import random
n = 2
i = 0
list = []
while n > i:
    list.append(random.randint(0, 10))
    i+=1
print(list)
print(f"подсказка Пети № 1 - произведение загаданных числес равно: {list[0]*list[1]}")
print(f"подсказка Пети № 2 - сумма загаданных числес равна: {list[0]+list[1]}")
x = int(input('введите первое число: '))
y = int(input('введите второе число: '))
flag = False
j=0
k=0
if x==list[0] or y==list[0]:
    j=1
if x==list[1] or y==list[1]:
    k=1
if j==1 and k==1:
    flag=True
if flag==False:
    print('Эх Катя-Катя!')
else: print('Катя молодец')

print(f'Петя загадал {list}')
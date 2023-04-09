import random
n = int(input("Введите кол-во монеток: "))
i = 0
list = []
while n > i:
    list.append(random.randint(0, 1))
    i+=1
print(list)
min1=0
min2=0

for j in range (n):
    if list[j] == 0:
        min1=min1+1
    else:
        min2=min2+1
print(f'монеток вверх решкой {min1}, а вверх гербом {min2}')
if min1>min2:
    for k in range (n):
        if list[k]==1:
            list.insert(k,0)
            list.remove(1)
else: 
    for l in range(n):
        if list[l]==0:
            list.insert(l,1)
            list.remove(0)

print(list)
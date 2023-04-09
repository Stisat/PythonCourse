n = int(input('введите число N: '))
i=int(0)
fl=False
lis1 = []
while fl==False:
    x = 2**i
    lis1.append(x)
    if lis1[i]>n:
        fl=True
    i+=1    
print(lis1[0:i-1])
    

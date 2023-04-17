# *****Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

# Input -> 435467
# Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь

print("Введите число: ")
number = int(input())
text = ''

listNumW =[{0:'',1:'один', 2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'},
{0:'десять',1:'одиннадцать',2:'двенадцать',3:'тринадцать',4:'четырнадцать',5:'пятнадцать',6:'шестнадцать',7:'семнадцать',
8:'восемнадцать',9:'девятнадцать'},
{2:'двадцать',3:'тридцать',4:'сорок',5:'пятьдесят', 6:'шестьдесят',7:'семьдесят',8:'восемьдесят',9:'девяноста'},
{1:'сто',2:'двести',3:'триста',4:'четыреста',5:'пятьсот',6:'шестьсот',7:'семьсот',8:'восемьсот',9:'девятьсот',},
{1:'одна тысяча', 2:'две тысячи',3:'три тысячи',4:'четыре тысячи',5:'пять тысяч',6:'шесть тысяч',7:'семь тысяч',8:'восемь тысяч',9:'девять тысяч'},]

if 99999<number<1000000:
    dict3 = dict(listNumW[3])
    numtemp = number//100000
    numtemp1 = number//1000
    if numtemp1%10==0:
        text = text+str(dict3[numtemp])+' '+'тысяч'+' '
    else:    
        text = text+str(dict3[numtemp])+' '
    number=number%100000
if 19999<number<100000:
    dict2 = dict(listNumW[2])
    numtemp = number//10000
    numtemp1 = number//1000
    if numtemp1%10==0:
        text = text+str(dict2[numtemp])+' '+'тысяч'+' '
    else:    
        text = text+str(dict2[numtemp])+' '
    number=number%10000
if 10000<number<20000:
    dict1 = dict(listNumW[1])
    numtemp = (number//1000)%10
    text = text+str(dict1[numtemp])+' '+'тысяч'+' '
    number=number%1000
if 999<number<10000:
    dict4 = dict(listNumW[4])
    text = text+str(dict4[number//1000])+' '
    number=number%1000
if 99<number<1000:
    dict3 = dict(listNumW[3])
    text = text+str(dict3[number//100])+' '
    number=number%100
if number<100:
    if 19<number<100:
        dict2 = dict(listNumW[2])
        text = text+str(dict2[number//10])+' '
    if 9<number<20 or number>99:
        dict1 = dict(listNumW[1])
        text = text+str(dict1[number%10])+' '
    if number<10 or number>19:
        dict0 = dict(listNumW[0])
        text = text+str(dict0[number%10])+' '

print(text)
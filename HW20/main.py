# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,которое содержит либо только английские,
# либо только русские буквы.
import string
flag = False
count = 0
eng=2
print('Введите текст для игры только на русском или английском языке:')
text = str(input())
while flag == False:
    if text.isalpha() == flag:
        print('Введенный текст не должен содержать цифр, введите текст еще раз: ')
        text = str(input())
        flag = False
    else:
        flag = True

if ascii(text)==(f"'{text}'"):
    eng=1
else:
    for v in range(len(text)):
        if ascii(text[v])!=(f"'{text[v]}'"):
            count=count+1
if count==len(text):
    eng=0

EngSymPoint = {'A,E,I,O,U,L,N,S,T,R': 1, 'D,G': 2, 'B,C,M,P': 3, 'F,H,V,W,Y': 4, 'K': 5, 'J,X': 8, 'Q,Z': 10}
RuSymPoint = {'А,В,Е,И,Н,О,Р,С,Т': 1, 'Д,К,Л,М,П,У': 2, 'Б,Г,Ё,Ь,Я': 3, 'Й,Ы': 4, 'Ж,З,Х,Ц,Ч': 5, 'Ш,Э,Ю': 8, 'Ф,Щ,Ъ': 10}

def SumPoint(t, dict):
    t=t.upper() 
    point = 0
    col = []
    for i in dict:
        col.append(i)
    for j in range(len(col)):
        for l in col[j]:
            for h in range(len(t)):
                if t[h]==l:
                    point = point + dict[col[j]]
    return point

if eng ==1:
    print(f'количество очков за английские символы равно: {SumPoint(text, EngSymPoint)}')
if eng ==0:
    print(f'количество очков за русские символы равно: {SumPoint(text, RuSymPoint)}')
if eng ==2:
    print('в тексте применены смешанные русские и английские символы, игра не засчитана')
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def addDict():
    collect = {}
    d=1
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for l in file:
            l=l.replace('\n','')
            collect[d]=list(l.split(';'))
            d=d+1
    return collect
dictPhone = addDict()
def findNumber(dict1):
    find = str(input('Введите ваш запрос для поиска (регистр учитывается): '))
    for i in dict1:
        for j in range(len(dict1[i])):
            if find in dict1[i][j]:
                print(f'{i}) {dict1[i]}')
    print('Что желаете сделать?')
    print('1 - оставить без изменений.')
    print('2 - удалить запись.')
    print('3 - изменить запись.')
    n= int(input('Выберите вариант: '))
    if n==1:
        choice(dict1)
    if n==2:
        deleteNum()
        print('Отображаю обновлённый справочник: ')
        getPhone(dictPhone)
        choice(dict1)
    if n==3:
        changeNum()
        print('Отображаю обновлённый справочник: ')
        getPhone(dictPhone)
        choice(dict1)
def deleteNum():
    n = int(input('выберите № записи для удаления: '))
    dictPhone.pop(n)
    addDict()
    addFile()
def changeNum():
    n = int(input('выберите № записи для изменения: '))
    dictPhone[n] = list(input('Ввведите Фамилию, Имя и № телефона через пробел: ').split())
    addDict()
    addFile()
def getPhone(dictP):
    for i in dictP:
        print(f'{i}) {dictP[i]}')
def addPhone():
    s=1
    save = list(input('Ввведите Фамилию, Имя и № телефона через пробел: ').split())
    while True:
        if s in dictPhone:
            s=s+1
        else:
            dictPhone[s] = save
            addFile()
            break
def addFile():
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for k in dictPhone:
            file.write(f'{dictPhone[k][0]};{dictPhone[k][1]};{dictPhone[k][2]}\n')    
def choice(dict):
    print('Выберите действие с телефонным справочником от 1 до 4:')
    print('1 - Показать справочник, 2 - Произвести поиск по запросу, 3 - Добавить данные в справочник, 4 - Выход')
    n = int(input('Ваш выбор: '))
    if n==1:
        getPhone(dict)
        choice(dict)
    if n==2:
        findNumber(dict)
    if n==3:
        addPhone()
        getPhone(dict)
        choice(dict)
    if n==4:
        print('До Свидания!')
    if 1<n and n>4:
        print('Не верный выбор, попробуйте еще раз:')
        choice(dictPhone)

print('Здравствуйте')
choice(dictPhone)
import random
ticketNumber = random.randint (100000, 999999)
print(f"Во время поездки в общественном транспорте вы получили билет с №: {ticketNumber}")
print()
size = 6
i = 0
collect = []
while i<size:
    temp = ticketNumber % 10
    collect.append(temp)
    ticketNumber = ticketNumber//10
    i=i+1
collect.reverse()
i = 0
sum1 = 0
sum2 = 0 
while i < (size/2):
    sum1 = sum1 + collect[i]
    sum2 = sum2 + collect[-1-i]
    i = i + 1
if sum1 == sum2:
    print("Да у Вас счастливый билет!!!")
else: print("Ну какой есть, жаль что не счастливый")
#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Кол-во монет: "))
avers = 0
revers = 0
for _ in range(n):
    x = int(input('аверс (1) или реверс (0)? '))
    if x == 1:
        avers += 1
    else:
        revers += 1
print(avers if avers < revers else revers)

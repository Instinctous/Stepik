# Ведьмак принимает монеты номиналом 1, 5, 10, 25
# Напишите программу, которая выводит минимальное количество монет при вводе суммы.
a = int(input())
counter = 0
while a >= 25:
    counter += 1
    a = a - 25
while a >= 10:
    counter += 1
    a = a - 10
while a >= 5:
    counter += 1
    a = a - 5
while a >= 1:
    counter += 1
    a = a - 1
print(counter)
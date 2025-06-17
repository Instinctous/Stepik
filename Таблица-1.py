# Дано натуральное число n (n < 9). Необходимо напечатать таблицу размером n x 3, состоящую из данного числа (между ними 1 пробел)
num = int(input())
for i in range(num):
    for j in range(3):
        print(num, end=' ')
    print()
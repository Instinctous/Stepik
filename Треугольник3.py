# Дано натуральное число. Напишите программу,которая печатает численный треугольник с высотой, равной n,по примеру:
# 1
# 121
# 12321
# 1234321
num = int(input())
for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(col, end='')
    for col in range(row - 1, 0, -1):
        print(col, end='')
    print()
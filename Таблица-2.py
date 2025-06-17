# Дано натуральное число n (n < 9). Необходимо вывести таблицу размером n x 5, где в i-строке указано число i (числа через пробел)
num = int(input())
for i in range(1, num + 1):
    for j in range(5):
        print(i, end=' ')
    print()
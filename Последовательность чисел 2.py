# Даны 2 целых числа m и n. Напишите программу,которая вывод все целые числа
# от m до n включительно в порядке возастания. Если m < n, то в порядке убывания
# если m == n, вывести m.
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
        for i in range(m, n - 1, - 1):
            print(i)
else:
    print(m)
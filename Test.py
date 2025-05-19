m = int(input())
n = int(input())
if m > n:
    for i in range(n, m + 1):
        print(i)
if m < n:
    for i in range(m, n + 1):
        print(i)
if m == n:
    print(m)

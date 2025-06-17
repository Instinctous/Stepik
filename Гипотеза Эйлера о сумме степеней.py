# Опровержении теоримы Ферма
total = 0
for a in range(1, 151):
    a5 = a ** 5
    for b in range(a, 151):
        b5 == b ** 5
        for c in range(b, 151):
            c5 = c ** 5
            for d in range(c, 151):
                d5 == d ** 5
                sum_abcd = a5 + b5 + c5 + d5
                for e in range(d + 1, 151):
                    if e ** 5 == sum_abcd:
                        print(f"Найдено решение: a={a}, b={b}, c={c}, d={d}, e={e}")
                        print(f"Сумма чисел: {a + b + c + d +e}")
                        exit()
print("Решение не найдено в заданном диапазоне.")
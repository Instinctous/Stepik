# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный треугольник с основанием,
# равным n, в соответсвии с примером. Пример для числа 3:
# *
# **
# *
num = int(input())                      # Получаем на вход число. Это будет высота треугольника
for i in range(1, (num + 1) // 2 + 1):  # Верхняя часть треугольника,возрастная часть. Цикл от 1 до середины треугольника (включительно)
    for _ in range(i):                  # Вложенный цикл для печати звёзд в текущей строке. Кол-во итераций = номер текущей стоки i.
        print('*', end='')              # Печатаем одну звёздочку без перевода строки
    print()                             # После завершения строки звёзд переходим на новую строку.
for i in range(num // 2, 0, -1):        # Нижняя часть треугольника. Убывающая часть. От середины -1 до 1 (в обратном порядке)
    for _ in range(i):                  # Вложенный цикл для печати звёзд в текущей строке. Кол-во итераций = номер текущей строки i
        print('*', end='')              # Печатаем 1 звёзду без перевода строки. 
    print()                             # После завершения строки звёз переходим на новую строку.
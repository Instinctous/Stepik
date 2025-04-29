try:
    name = input("Как тебя зовут? ")
    age = int(input("Сколько тебе лет? "))
    print(f"{name}, ты начал свой путь в Python. Дерзай!")
    if age < 18:
        print("Ты молод! Начинать рано — это преимущество.")
    else:
        print("Никогда не поздно!")
except ValueError:
    print("Ошибка: введите число для возраста!")

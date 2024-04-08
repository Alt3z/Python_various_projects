def hardash_cheak(x): # функция для определения является ли число числом Хардаша
    summa = sum(int(i) for i in str(x)) # суммируем все цифры
    return x % summa == 0

def get_hardash_numbers(start, n): # функция для нахождения n числе Хардаша начиная с start
    hardash = []
    count = 0
    while count != n:
        if hardash_cheak(start): # если вернулось True
            hardash.append(start)
            count += 1
        start += 1
    return hardash

x = int(input("Введите число для проверки: "))
print(f"Является ли число {x} число Хардаша: {hardash_cheak(x)}")

start = int(input("Введите число с которого начнутся искаться числа Хардаша: "))
n = int(input("Введите количество чисел Харадаша, которые вы хотите найти: "))
print(f"{n} чисел/числа Хардаша начиная с {start}: {', '.join(map(str, get_hardash_numbers(start, n)))}")
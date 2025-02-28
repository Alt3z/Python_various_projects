n, k = map(int, input().split())
values = sorted(input().split(), key=int)

total_sum = sum(int(value) for value in values)
max_digit = len(max(values, key=len))  # Максимальная длина числа
count = 0

while k > 0 and max_digit > 0:
    check_list = []
    index = []

    # Формируем список чисел, где длина >= max_digit
    for i in range(len(values) - 1, -1, -1):
        if len(values[i]) >= max_digit:
            check_list.append(values[i])
            index.append(i)
        else:
            break

    # Сортируем по текущему разряду
    check_list = sorted(check_list, key=lambda x: x[len(x) - max_digit])

    # Применяем операции
    for i in range(len(check_list)):
        x = list(check_list[i])
        if k > 0:
            # Изменяем текущий разряд на 9, если он не равен 9
            if x[len(x) - max_digit] != '9':
                x[len(x) - max_digit] = '9'
                k -= 1
        check_list[i] = ''.join(x)

    # Обновляем значения в исходном массиве
    for i in range(len(check_list)):
        values[index[i]] = check_list[i]

    max_digit -= 1
    count += 1

total_sum_end = sum(int(value) for value in values)
print(total_sum_end - total_sum)

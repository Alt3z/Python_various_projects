def filter_numbers(numbers):
    numbers = sorted(numbers, reverse=True)

    result = []
    for i in range(len(numbers)):
        is_divisible = False
        for j in range(i):
            if numbers[j] % numbers[i] == 0:
                is_divisible = True
                break
        if not is_divisible:
            result.append(numbers[i])

    return result


n, x, y, z = map(int, input().split())
values = list(map(int, input().split()))

xyz = filter_numbers([x, y, z])


best = [10**7, 10**7, 10**7]

for value in values:
    for i in range(len(xyz)):
        change = 0
        x = value
        while x % xyz[i] != 0:
            x += 1
            change += 1
        if change < best[i]:
            best[i] = change

res = 0
for num in best:
    if num < 10**7:
        res += num

print(res)
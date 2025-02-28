interesting_numbers = []
for k in range(1, 10):
    num = k
    while num <= 10**18:
        interesting_numbers.append(num)
        num = num * 10 + k

l, r = map(int, input().split())

count = sum(1 for num in interesting_numbers if l <= num <= r)

print(count)
def f(p, m):
    res = 0
    for value in m:
        res += (value ** p) % 998244353

    return res

n, k = map(int, input().split())
values = list(map(int, input().split()))

all_values = []
for i in range(n):
    for j in range(i+1, n):
        all_values.append(values[i] + values[j])

for i in range(1, k+1):
    print(f(i, all_values))
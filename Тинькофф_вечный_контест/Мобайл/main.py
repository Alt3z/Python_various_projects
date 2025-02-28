def calculate_cost(a, b, c, d):
    if d <= b:
        return a
    else:
        return a + (d - b) * c

a, b, c, d = map(int, input().split())

print(calculate_cost(a, b, c, d))
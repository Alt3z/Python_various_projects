def min_parts(a, s):
    count = 1
    current_sum = 0

    for length in a:
        if current_sum + length > s:
            count += 1
            current_sum = 0
        current_sum += length

    return count

def solve(n, s, a):
    result = 0

    for l in range(n):
        current_sum = 0
        for r in range(l, n):
            current_sum += a[r]
            if current_sum > s:
                result += min_parts(a[l:r+1], s)
            else:
                result += 1

    return result


n, s = map(int, input().split())
a = list(map(int, input().split()))

print(solve(n, s, a))
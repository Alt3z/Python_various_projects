def is_collinear(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

def max_happy_triples(n, points):
    triples = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if not is_collinear(points[i][0], points[i][1],
                                    points[j][0], points[j][1],
                                    points[k][0], points[k][1]):
                    triples.append((i, j, k))

    max_count = 0
    used = [False] * n

    def backtrack(index, count):
        nonlocal max_count
        if index == len(triples):
            max_count = max(max_count, count)
            return
        i, j, k = triples[index]
        if not (used[i] or used[j] or used[k]):
            used[i] = used[j] = used[k] = True
            backtrack(index + 1, count + 1)
            used[i] = used[j] = used[k] = False
        backtrack(index + 1, count)

    backtrack(0, 0)
    return max_count


n = int(input())
points = [tuple(map(int, input().split())) for i in range(n)]

print(max_happy_triples(n, points))
import math

def min_cuts(n: int):
    if n == 1:
        return 0
    return math.ceil(math.log2(n))


n = int(input())

print(min_cuts(n))
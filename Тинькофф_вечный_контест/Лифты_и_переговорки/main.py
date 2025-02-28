n, t = map(int, input().split())
levels = list(map(int, input().split()))
leaver = int(input())

if t > max(levels):
    print(max(levels) - min(levels))
elif (levels[leaver-1] - min(levels) < t) or (max(levels) - levels[leaver-1] < t):
    print(max(levels) - min(levels))
else:
    down = levels[leaver-1] - min(levels) + max(levels) - min(levels)
    up = max(levels) - levels[leaver-1] + max(levels) - min(levels)
    print(min(down, up))
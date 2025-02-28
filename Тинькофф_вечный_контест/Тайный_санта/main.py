n = int(input())
values = list(map(int, input().split()))

if len(set(values)) + 1 != len(values):
    print(-1, -1)
else:
    for i in range(1, n+1):
        if i not in values:
            not_in_values = i
            break

    flag = False
    for i in range(n):
        for j in range(i+1, n):
            if values[i] == values[j]:
                if i+1 != not_in_values:
                    not_unique = i + 1
                else:
                    not_unique = j + 1
                flag = True
                break
        if flag == True:
            break

    print(not_unique, not_in_values)
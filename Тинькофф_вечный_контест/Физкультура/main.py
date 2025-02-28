n = int(input())
values = list(map(int, input().split()))

index_poz = []
index_neg = []

for i in range(n):
    if (i == 0 or i % 2 == 0) and (values[i] % 2 == 0):
        index_neg.append(i)
    elif (i % 2 == 1) and (values[i] % 2 != 0):
        index_poz.append(i)

if len(index_poz) == 1 and len(index_neg) == 1:
    if index_poz[0] > index_neg[0]:
        print(index_neg[0] + 1, index_poz[0] + 1)
    else:
        print(index_poz[0] + 1, index_neg[0] + 1)
elif len(index_poz) == 0 and len(index_neg) == 0:
    if len(values) > 2:
        print(1, 3)
    else:
        print(-1, -1)
else:
    print(-1, -1)
n, m = map(int, input().split())
values = list(map(int, input().split()))

first_day = values[0]
second_day = values[1]

flag = False

count = 0
bad_day_first = []
bad_day_sec = []

for i in range(2, n):
    if count == m:
        print(0)
        flag = True
        break

    if (values[i] >= first_day) and (values[i] <= second_day):
        count += 1
    elif values[i] < first_day:
        bad_day_first.append(values[i])
    else:
        bad_day_sec.append(values[i])

if not flag:
    bad_day_first.sort()
    bad_day_sec.sort()

    index_first = 0
    index_second = 0

    change = 0
    while count != m:
        if index_first < len(bad_day_first) and index_second < len(bad_day_sec):
            if (first_day - bad_day_first[index_first]) < (bad_day_sec[index_second] - second_day):
                change += first_day - bad_day_first[index_first]
                index_first += 1
            else:
                change += bad_day_sec[index_second] - second_day
                index_second += 1
        elif index_first < len(bad_day_first):
            change += first_day - bad_day_first[index_first]
            index_first += 1
        else:
            change += bad_day_sec[index_second] - second_day
            index_second += 1
        count += 1

    print(change)
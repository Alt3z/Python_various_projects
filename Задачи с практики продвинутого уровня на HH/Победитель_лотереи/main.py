def next_smaller(n):
    m = [int(i) for i in n]

    for i in range(len(n)-1, 0,-1):
        if i==1 and m[i] == 0:
            return -1
        elif m[i] < m[i-1]:
            temp = m[i]
            m[i] = m[i-1]
            m[i-1] = temp
            return ''.join(map(str, m))
    return -1


input_string = input()
result = next_smaller(input_string)
print(result)


'''
input_string = ["123","101","531","1020","256","896", "526", "505", "1060000"]
for num in input_string:
    print(f"Для {num}: {next_smaller(num)}")
'''
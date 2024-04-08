def palindrome_check_1(s):
    s = ''.join(filter(str.isalnum, s.lower())) # приводим всю строку к нижнему регистру и оставляем только то, что является цифрой или буквой
    flag = True
    for i in range(int(len(s) / 2)): # проход по половине предложения
        if s[i] != s[-i - 1]: # если символы не совпадают
            flag = False
            print("Предложение не является палиндромом")
            break
    if (flag == True):
        print("Предложение является палиндромом")

def palindrome_check_2(s):
    s = ''.join(filter(str.isalnum, s.lower()))
    if (s == s[::-1]): # проверяем ялвляется ли строка равной обратной самой себе
        print("Предложение является палиндромом")
    else:
        print("Предложение не является палиндромом")

palindrome_check_1("А Роза упала на лапу азора")
palindrome_check_1("скоро выпадет снег")

print()

palindrome_check_2("А Роза упала на лапу азора")
palindrome_check_2("скоро выпадет снег")
number = int(input('Введите число: '))
word = input('Введите строку: ')
for i in word:
    if (1039 <= ord(i) <= 1105):
        i = chr(ord(i) - (32 - number))
    print(i.lower(), end="")
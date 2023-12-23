N = int(input('Введите количество строк: '))
strings = list()
for i in range(N):
    string = input('Введите строку: ')
    strings.append(string)
sorted_strings = sorted(strings)
for string in sorted_strings:
    print(string)
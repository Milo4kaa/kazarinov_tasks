N = int(input('Введите количество школьников:'))
str = list()
sstr = list()
for i in range(N):
    string = input('Введите ученика и оценку: ')
    str.append(string)
    if 4 >= int(string.split()[1]) <=5: sstr.append(string)
for i in str: print(i)
print()
for i in sstr: print(i)


game = input('Введите строку: ')
orel = 0
max = 0
for i in game:
    if i == 'о':
        orel += 1
        if orel > max:
            max = orel
    else:
        orel = 0
print(max)

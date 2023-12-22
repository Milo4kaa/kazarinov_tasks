x = 0
z = 0
numstr = -1
stroka = ''
while stroka != 'стоп':
    x += 1
    stroka = input('Введите строку: ').lower()
    if 'кот' in stroka:
        if numstr < 0:
            numstr = x
        z += 1
print(z,numstr)

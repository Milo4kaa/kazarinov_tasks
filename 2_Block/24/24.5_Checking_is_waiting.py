test_string = '''
3   3144
15     *3   =45
100    *1   =100
2999   *1   =2999

'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

import re

number = input('Введите количество позиций и общую сумму: ')
lst = number.split()
kolv = int(lst[0])
sum = int(lst[1])
sumk = 0
errors = list()
for i in range(kolv):
    stroka = input('Введите строку: ')
    zx = re.split('[*=]', stroka)
    if int(zx[0]) * int(zx[1]) == int(zx[2]):
        sumk += int(zx[2])
    else:
        errors.append(i+1)
print(sum-sumk)
for i in errors: print(i)
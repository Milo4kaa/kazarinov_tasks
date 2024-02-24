test_string = '''
5
Кузнецов	5
Круглов	4
Федин	4
Тарасов	2
Словецкий	3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

N = int(input('Введите количество школьников:'))
str = list()
sstr = list()
for i in range(N):
    strin = input('Введите ученика и оценку: ')
    str.append(strin)
    if int(strin.split()[1]) >= 4:  sstr.append(strin)
for i in str: print(i)
print()
for i in sstr: print(i)


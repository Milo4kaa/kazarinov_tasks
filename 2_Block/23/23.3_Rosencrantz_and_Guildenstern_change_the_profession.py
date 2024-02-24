test_string = '''
рооррооор
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

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

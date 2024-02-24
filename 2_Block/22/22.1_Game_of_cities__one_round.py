test_string = '''
париж
житомир
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

frst = input('Введите первый город: ')
scnd = input('Введите второй город: ')
if frst[-1] == scnd[0]:
    print('Верно')
else:
    print('Неверно')
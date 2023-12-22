test_string = '''
пароль
пароль
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
     if prompt:
        print(prompt)
     tmp = test_string.pop()
     print(tmp)
     return tmp

psw1 = input('Введите пароль: ')
psw2 = input('Повторите пароль: ')
if len(psw1) < 8:
    print('Пароль слишком короткий.')
else:
    if psw1 == psw2:
        print('OK')
    else:
        print('Различаются')

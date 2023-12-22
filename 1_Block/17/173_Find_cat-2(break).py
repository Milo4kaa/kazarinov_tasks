test_string = '''
Как устроен типичный фрукт:
кожура;
мякоть;
косточки.
стоп
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

x = 0
stroka = ''
while stroka != 'стоп':
    x += 1
    stroka = input('Введите строку: ').lower()
    if 'кот' in stroka:
        print(x)
        break
if not 'кот' in stroka:
    print(-1)
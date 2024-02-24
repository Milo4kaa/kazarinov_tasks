test_string = '''
4
три
четыре
пять
шесть
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

N = int(input('Введите количество строк: '))
strings = list()
for i in range(N):
    string = input('Введите строку: ')
    strings.append(string)

sorted_strings = sorted(strings, key=lambda x: (len(x), x))
for string in sorted_strings:
    print(string)


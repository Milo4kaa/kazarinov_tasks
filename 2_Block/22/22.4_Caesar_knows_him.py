test_string = '''
5
На дворе трава, на траве дрова!
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

number = int(input('Введите число: '))
word = input('Введите строку: ')
for i in word:
    if (1039 <= ord(i) <= 1105):
        i = chr(ord(i) - (32 - number))
    print(i.lower(), end="")
test_string = '''
Баобаб
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

from collections import Counter

s = input('Vvedite slovo: ').lower()
for c, n in Counter(s).most_common(1):
    print(c)
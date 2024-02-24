test_string = '''
Раз два три
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

words = input().split()
symb = 0
for i in words:
    symb += len(i)
print(symb)
test_string = '''
#2
name = input()  
print('Привет,', name) # здороваемся
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

lst = list()
for i in range(int(input()[1])):
    stroka = input()
    if '#' in stroka:
        stroka = stroka.split('#')[0]
        lst.append(stroka)
    else: lst.append(stroka)
[print(i) for i in lst]


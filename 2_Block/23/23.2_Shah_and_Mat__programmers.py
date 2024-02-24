test_string = '''
4
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

number = int(input('Введите размер доски: '))
symb = 'ABCDEFGH'
for i in range(number, 0, -1):
    for j in symb[0:number]:
        print(j,i,sep="",end=" ")
    if j == symb[number-1]:
        print()


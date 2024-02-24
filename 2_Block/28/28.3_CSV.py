test_string = '''
4
Дама,сдавала в багаж,
диван, чемодан, саквояж
картину, корзину, картонку
и маленькую собачонку,,
4
0,0
1,2
3,1
3,0
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

words = []
for i in range(int(input('Chislo: '))):
    stroka = input('Stroka: ').split(',')
    words.append(stroka)
for i in range(int(input('Chislo: '))):
    cords = [int(i) for i in input('Kord: ').split(',')]
    d = words[cords[0]]
    word = d[cords[1]]
    print(word)
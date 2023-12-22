test_string = '''
10
10
1
5
2
10
1
5
'''.strip().split('\n')[::-1]
def input(prompt=''):   
    if prompt:
        print(prompt) 
    tmp = test_string.pop()
    print(tmp)
    return tmp

def play_nim():
    first_pile = int(input('Введите количество камней в первой руке:'))
    second_pile = int(input('Введите количество камней во второй руке:'))
    
    while True:
        
        print('В первой куче:',first_pile,'Во второй куче:',second_pile)
    
        if first_pile == 0 and second_pile == 0:
            break

        pile_num = int(input('Из какой кучи возьмём:'))
        num_stones = int(input('Количество камней:'))

        if pile_num == 1:
            first_pile -= num_stones
        elif pile_num == 2:
            second_pile -= num_stones
    
play_nim()

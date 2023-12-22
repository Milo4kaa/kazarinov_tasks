test_string = '''
2
раз
два
три
четыре
раз
двыа
раз
два
три
три
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

patience = int(input('Введите число: '))
indication = 0
while patience:
    for counting in ('раз', 'два', 'три', 'четыре'):
        if counting == input():
            indication += 1
        else:
            print(f'Правильных отсчётов было {indication}, но теперь вы ошиблись.')
            indication = 0
            patience -= 1
            break
print('На сегодня хватит')
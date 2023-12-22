test_string = '''
6
С кем война?
С кем мир?
Меняем
С кем война?
Меняем
С кем война?
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

c = "Евразия"
x = "Остазия"
number = 1
greek_letter_2 = int(input('Введите к-во вопросов: '))

while number <= greek_letter_2:
    number += 1
    greek_letter_1 = input("Введите вопрос: ")
    if greek_letter_1 == "С кем война?":
        print(c)
    if greek_letter_1 == "С кем мир?":
        print(x)
    if greek_letter_1 == "Меняем":
        c,x = x,c

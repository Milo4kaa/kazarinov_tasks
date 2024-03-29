test_string = '''
2
2
2
Иванов
Петров
Сидоров
Иванов
Петров
Иванов
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()


eng = int(input('Введите число учеников изучающих английский язык: '))
print(eng)
ger = int(input('Введите число учеников изучающих немецкий язык: '))
print(ger)
fr = int(input('Введите число учеников изучающих французский язык: '))
print(fr)

students = {}
two = {}

for i in range(eng + ger + fr):
    name = input('Введите фамилию ученика: ')
    print(name)

    if name in students:
        students[name] += 1
        if students[name] == 2:
            two[name] = 1
    else:
        students[name] = 1

if len(two) > 0:
    print(len(two))
else:
    print('NO')
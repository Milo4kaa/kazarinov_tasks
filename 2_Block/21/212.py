test_string = '''
3
3
Иванов
Петров
Васечкин
Иванов
Петров
Васечкин
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

eng = int(input('Введите число учеников, изучающих английский язык: '))
print(eng)
ger = int(input('Введите число учеников, изучающих немецкий язык: '))
print(ger)
students = set()

for i in range(eng + ger):
    pupil = input('Введите фамилию ученика: ')
    print(pupil)
    students.add(pupil)

unique_students = len([student for student in students if students.add(student) == 1])

if unique_students == 0:
    print('NO')
else:
    print(unique_students)

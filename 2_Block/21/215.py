test_string = '''
6
Иванов
Петров
Сидоров
Петров
Иванов
Петров
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

N = int(input('Введите количество мужчин-сотрудников: '))
print(N)
members = set()
duplicates = set()
for i in range(N):
    name = input('Введите фамилию: ')
    print(name)
    if name in members:
        duplicates.add(name)
    else:
        members.add(name)
print(N-(len(members)-len(duplicates)))

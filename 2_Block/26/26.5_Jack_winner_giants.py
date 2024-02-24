test_string = '''
3
Просто
Приятный  Парень
*
Самый
Продуктивный
  Выращиватель
Бобов
*
Джек
Победитель Великанов
*
 '''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

n = int(input("Введите количество титулов: "))

titles = []
for _ in range(n):
    title_lines = []
    line = input()
    while line != '*':
        title_lines.append(line)
        line = input()
    titles.append('-'.join(' '.join(title_lines).split()))

print("Ответ:\n"+','.join(titles[::-1]))

test_string = '''
4
4
Хоббит
Алиса в стране чудес
Том Сойер
Остров сокровищ
Буратино
Хоббит
Остров сокровищ
Война и мир
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

N = 0
M = 0
while N < 1 or M <1:
    N = int(input('Введите число книг в домашней библиотеке: '))
    print(N)
    M = int(input('Введите число книг заданных на лето: '))
    print(M)
home = set()
for i in range(N):
    book = input('Введите книгу в домашней библиотеке: ')
    print(book)
    home.add(book)
for i in range(M):
    book = input('Введите книгу заданную на лето: ')
    print(book)
    if book in home:
        print('Yes')
    else:
        print('No')



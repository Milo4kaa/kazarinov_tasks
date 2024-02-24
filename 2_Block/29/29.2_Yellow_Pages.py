test_string = '''
3
101010 Ваня
79076192073 Коля
79234120156 Ваня
3
Коля
Ваня
Олег
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

def main():
    n = int(input())
    phone_book = {}

    for _ in range(n):
        number, name = input().split()
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]

    m = int(input())
    queries = [input() for _ in range(m)]

    for query in queries:
        if query in phone_book:
            print(' '.join(phone_book[query]))
        else:
            print('Нет в телефонной книге')

main()
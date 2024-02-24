test_string = '''
4
Ваня 20 янв
Петя 15 июн
Вася 10 янв
Коля 20 июл
3
июн
дек
янв
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

def main():

    n = int(input())
    birthdays = {}


    for _ in range(n):
        name, day, month = input().split()
        if month in birthdays:
            birthdays[month].append(name)
        else:
            birthdays[month] = [name]

    m = int(input())
    queries = [input() for _ in range(m)]

    for query in queries:
        if query in birthdays:
            names = birthdays[query]
            names.sort()
            print(' '.join(names))
        else:
            print()

if __name__ == "__main__":
    main()
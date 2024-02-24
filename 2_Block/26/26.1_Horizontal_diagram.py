test_string = '''
3 7 1 10 8
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

numbers = input("Введите натуральные числа, разделённые пробелами: ").split()

for num in numbers:
    print('*' * int(num))
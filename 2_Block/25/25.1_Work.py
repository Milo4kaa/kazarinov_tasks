test_string = '''
4
37
3
99
55
111
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

n = int(input('Введите количество чисел в наборе:'))
numbers = list()
for i in range(n):
    num = int(input('Введите число: '))
    numbers.append(num)
target = int(input('Введите конечное число: '))
z = False
for num in numbers:
    res = target / num
    if res in numbers and num != res:
        z = True
if z:
    print("ДА")
else:
    print("НЕТ")
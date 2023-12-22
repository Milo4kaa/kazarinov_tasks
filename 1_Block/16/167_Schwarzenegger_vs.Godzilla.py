test_string = '''
3
1
2
1
3
1
3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

num_fractions = int(input("Введите количество дробинок: "))
total_num = 0
total_den = 1
while num_fractions > 0:
    num = int(input("Введите числитель дробинки: "))
    den = int(input("Введите знаменатель дробинки: "))
    num *= total_den
    total_num *= den
    total_num += num
    total_den *= den
    a, b = total_num, total_den
    while b != 0:
        a, b = b, a % b
    total_num //= a
    total_den //= a
    num_fractions -= 1
print(f"Суммарный урон: {total_num}/{total_den}")

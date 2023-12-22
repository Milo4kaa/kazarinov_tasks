height = int(input('Введите высоту пирамиды: '))
i = 0
while i < height:
    print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    i += 1
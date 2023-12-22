for num in range(1,20):
    x = 1
    print(f'Факториал {num}: ')
    while num > 0:
        x *= num
        num -= 1
    print(x)

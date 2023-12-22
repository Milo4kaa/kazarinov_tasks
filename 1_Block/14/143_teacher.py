print('Введите сколько денег у учителя:')
for a in range(150, 200):
    b = int(a)
    c = b / 8
    d = c / 8
    rounded_result = round(d)
    print(f'Денег у учителя {a}, осталось{rounded_result}')
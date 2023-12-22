test_string = '''
25
2000
370.35
-1
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
     if prompt:
        print(prompt)
     tmp = test_string.pop()
     print(tmp)
     return tmp

total = 0
print('Вводите цены; для остановки введите -1.')
price = float(input())
while price > 0:
    total = total + price
    price = float(input())
print('Общая стоимость равна', total)
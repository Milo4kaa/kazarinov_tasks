test_string = '''
5
Овсянка
Рис
Суп
МаннаяКаша
Рыба
2
3
Рис
Суп
Рыба
2
Рис
Рыба
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()

food = set()
g = set()
M = int(input('Введите число блюд, которые может приготовить столовая: '))
print(M)
for i in range(M):
    food_input = input('Введите блюдо: ')
    print(food_input)
    food.add(food_input)

N = int(input('Введите число дней, для которых есть список блюд: '))
print(N)
for i in range(N):
    d = int(input('Введите число блюд в данный день: '))
    print(d)
    for a in range(d):
        food_day = (input('Введите блюда на этот день: '))
        print(food_day)
        g.add(food_day)

for i in food - g:
    print(f"Блюда которые не готовили: {i}")

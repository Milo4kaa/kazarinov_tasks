test_string = '''
-2
9
вперёд
9
налево
вперёд
2
разворот
вперёд
17
стоп
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp


the_minimum_number_of_instructions = 0
x = int(input("Координаты клада по оси X"))
y = int(input("Координаты клада по оси Y"))
x1 = 0
y1 = 0
move = 'север'
direction_of_movement = input("Введите команду (вперед <шаги> или разворот), для завершения введите 'стоп': ")
while direction_of_movement != 'стоп':
    if int(x) == x1 and int(y) == y1:
        print(f"\nОтвет:\n{the_minimum_number_of_instructions}\n{move}")
        break
    else:
        the_minimum_number_of_instructions += 1
        if direction_of_movement == 'вперёд':
            steps = int(input("Количество указаний карты"))
            if move == 'север':
                y1 += steps
            elif move == 'запад':
                x1 -= steps
            elif move == 'юг':
                y1 -= steps
            elif move == 'восток':
                x1 += steps
        elif direction_of_movement == 'направо':
            if move == 'север':
                move = 'восток'
            elif move == 'восток':
                move = 'юг'
            elif move == 'юг':
                move = 'запад'
            elif move == 'запад':
                move = 'север'
        elif direction_of_movement == 'налево':
            if move == 'север':
                move = 'запад'
            elif move == 'запад':
                move = 'юг'
            elif move == 'юг':
                move = 'восток'
            elif move == 'восток':
                move = 'север'
        elif direction_of_movement == 'разворот':
            if move == 'север':
                move = 'юг'
            elif move == 'юг':
                move = 'север'
            elif move == 'запад':
                move = 'восток'
            elif move == 'восток':
                move = 'запад'
        direction_of_movement = input("Введите команду (вперед <шаги> или разворот), для завершения введите 'стоп': ")
else:
    if x == 0 and y == 0:
        print(0)
        print('север')

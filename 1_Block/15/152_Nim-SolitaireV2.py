test_string = '''
10
1
1
5
3
2
4
4
3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

def play_nim():
    print("Игра Ним")
    stones = int(input("Введите количество камней в куче: "))
    while stones > 0:
        player_choice = int(input("Сколько камней хотите взять (от 1 до 3)? "))
        if player_choice < 1 or player_choice > 3:
            print("Некорректный ход! Введите число от 1 до 3.")
            continue
        if player_choice > stones:
            print("Некорректный ход! Введите число не больше оставшегося количества камней.")
            continue
        stones -= player_choice
        print("В куче осталось", stones, "камней.")
    print("Игра окончена. Вы победили!")

play_nim()
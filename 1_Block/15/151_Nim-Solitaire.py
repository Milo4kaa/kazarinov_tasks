test_string = '''
20
1
1
5
3
2
4
4
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

def game_of_nim():
    stones = int(input("Введите количество камней в куче: "))
    while stones > 0:
        max_stones = min(stones, int(input("Сколько камней вы берете? ")))
        if max_stones < 1 or max_stones > stones:
            print("Некорректный ввод. Попробуйте еще раз!")
            continue
        stones -= max_stones
        print("Осталось камней:", stones)
    print("Игра окончена!")


game_of_nim()
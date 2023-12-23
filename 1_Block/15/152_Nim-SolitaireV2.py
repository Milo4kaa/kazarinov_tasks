
def play_nim(stones):
    print("Игра Ним")
    print("Количество камней в куче:", stones)
    while stones > 0:
        if stones % 4 == 0:
            computer_choice = 3
        else:
            computer_choice = stones % 4
        print("Компьютер взял", computer_choice, "камней.")
        stones -= computer_choice
        print("В куче осталось", stones, "камней.")
        if stones <= 0:
            print("Компьютер победил!")
            break

        if stones > 0:
            if stones % 4 == 0:
                player_choice = 1
            else:
                player_choice = stones % 4
            print("Игрок взял", player_choice, "камней.")
            stones -= player_choice
            print("В куче осталось", stones, "камней.")
            if stones <= 0:
                print("Вы победили!")
                break


for stones in range(1, 30):
    play_nim(stones)

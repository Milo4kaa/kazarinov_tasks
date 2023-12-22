test_string = '''
560
100
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

def buy_animals(subsidy, total_animals):
    for bulls in range(1, subsidy // 20 + 1):
        for cows in range((subsidy - bulls * 20) // 10 + 1):
            calves = total_animals - bulls - cows


            if (bulls * 20 + cows * 10 + calves * 5) == subsidy and calves >= 0:
                print(f"Быки: {bulls}, Коровы: {cows}, Телята: {calves}")


subsidy = int(input("Введите размер выделяемой субсидии в тыс. рублей: "))
total_animals = int(input("Введите количество голов скота, которое надо купить: "))

buy_animals(subsidy, total_animals)

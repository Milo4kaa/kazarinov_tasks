test_string = '''
5
лук 1 головка
картофелин штук 6
картошку почистить
лук порезать кольцами
зажарить всё
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

N = int(input("Введите количество пунктов рецепта: "))
recipe = []

for _ in range(N):
    ingredient = input()
    if 'лук' not in ingredient.lower():
        recipe.append(ingredient)

print("\n"+', '.join(recipe))

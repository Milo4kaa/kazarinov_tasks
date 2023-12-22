test_string = '''
2
вперёд
2
разворот
вперёд
1
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp


tunnel_length = int(input("Введите длину туннеля: "))
position = 0
steps_taken = 0

while True:
    command = input("Введите команду (вперед/разворот): ")
    if command == "вперед":
        steps = int(input("Введите количество шагов: "))
        if position + steps <= tunnel_length:
            position += steps
            steps_taken += 1
        else:
            break
    elif command == "разворот":
        steps_taken += 1
        break

print(f"Количество команд: {steps_taken}")


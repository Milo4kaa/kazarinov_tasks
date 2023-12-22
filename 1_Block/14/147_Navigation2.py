test_string = '''
2
1
вперёд
2
разворот
вперёд
1
стоп
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

def crawl_tunnel(tunnel_length, initial_position, commands):
    current_position = initial_position
    steps_count = 0

    for command in commands:
        action, *value = command.split()
        if action == "вперед":
            steps = int(value[0])
            if current_position + steps > tunnel_length:
                steps = tunnel_length - current_position
            current_position += steps
            steps_count += 1
        elif action == "разворот":
            current_position = tunnel_length - current_position
            steps_count += 1

    if current_position == tunnel_length:
        exit_side = "слева"
    else:
        exit_side = "справа"

    print(steps_count)
    print(exit_side)

tunnel_length = int(input("Введите длину туннеля: "))
initial_position = int(input("Введите начальную координату таракана: "))
commands = []

while True:
    command = input("Введите команду (вперед <шаги> или разворот), для завершения введите 'стоп': ")
    if command == 'стоп':
        break
    commands.append(command)

crawl_tunnel(tunnel_length, initial_position, commands)

test_string = '''
1
print     ('Привет')#поздороваемся
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp


def minimize_program(lines):
    minimized_lines = []
    in_quotes = False

    for line in lines:
        min_line = ''
        for i, char in enumerate(line):
            if char == '#':
                break
            elif char == '"':
                min_line += char
                if i > 0 and line[i - 1] != '\\':
                    in_quotes = not in_quotes
            elif char == ' ' and not in_quotes:
                if i == 0 or line[i - 1] != ' ':
                    min_line += char
            else:
                min_line += char

        minimized_lines.append(min_line)

    return minimized_lines


n = int(input())
input_lines = [input() for _ in range(n)]

minimized_program = minimize_program(input_lines)

for line in minimized_program:
    print(line)


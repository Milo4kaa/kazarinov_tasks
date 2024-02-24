test_string = '''
+++>+++++<-.>.>.-. 
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

def brain_explosion_program(program):
    tape = [0] * 30000
    pointer = 0
    output = []
    for command in program:
        if command == '>':
            pointer = (pointer + 1) % 30000
        elif command == '<':
            pointer = (pointer - 1) % 30000
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == '-':
            if tape[pointer] == 0:
                tape[pointer] = 255
            else:
                tape[pointer] = (tape[pointer] - 1) % 256
        elif command == '.':
            output.append(tape[pointer])
    return output

program = input().strip()
result = brain_explosion_program(program)
for value in result:
    print(value)


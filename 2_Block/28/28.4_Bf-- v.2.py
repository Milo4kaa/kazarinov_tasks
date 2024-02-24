test_string = '''
+.>.+>+>+>+++>+++++<[-].>.
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp
    
BAND_LEN = 10
def brain_explosion(program):
    stack = []
    memory = [0] * BAND_LEN
    pointer = 0
    output = []

    i = 0
    while i < len(program):
        command = program[i]

        if command == '>':
            pointer = (pointer + 1) % BAND_LEN
        elif command == '<':
            pointer = (pointer - 1) % BAND_LEN
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output.append(memory[pointer])
        elif command == '[':
            if memory[pointer] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    i += 1
                    if program[i] == '[':
                        open_brackets += 1
                    elif program[i] == ']':
                        open_brackets -= 1
            else:
                stack.append(i)
        elif command == ']':
            i = stack.pop() - 1

        i += 1

    return output

program = input().strip()

result = brain_explosion(program)
for out in result:
    print(out)


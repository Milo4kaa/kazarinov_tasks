test_string = '''
3 5 4 2
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

def max_height(columns):
    return max(columns) + 1

def print_diagram(columns):
    max_height_value = max_height(columns)
    diagonal_frame = " "
    for col in columns:
        diagonal_frame += "*"
    diagonal_frame += " "
    print(diagonal_frame)
    for i in range(max_height_value, 0, -1):
        row = "*"
        for col in columns:
            if col >= i:
                row += "*"
            else:
                row += " "
        print(row + "*")

input_numbers = list(map(int, input("Введите числа через пробел: ").split()))

print_diagram(input_numbers)
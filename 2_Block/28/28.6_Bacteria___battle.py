test_string = '''
3
5
5
5
5
5
5
5
5
5
1
1
0
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

n = int(input())
table = [[int(input()) for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    col, row = int(input()), int(input())
    table[row][col] -= 8
    for _row in range(-1, 2):
        for _col in range(-1, 2):
            if (0 <= col + _col <= n - 1) and (0 <= row + _row <= n - 1) and not (_row == 0 and _col == 0):
                table[row + _row][col + _col] -= 4
for item in table:
    print(*[el * (el >= 0) for el in item])
test_string = '''
3
2
тройка
треф
семёрка
червей
дама
пик
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

rows = int(input())
cols = int(input())
table = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(input())
    table.append(row)
for i in range(rows):
    for j in range(cols):
        print(table[i][j], end=' ')
    print()

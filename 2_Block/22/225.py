path = input('Введите символы: ')
simvol = path[0]
list = path[1:].split('V')
spaces = 0
for move in list:
    if move == '<':
        spaces -= len(move)
    print(' '*spaces + simvol*(1+len(move)))
    if move == '>':
        spaces += len(move)

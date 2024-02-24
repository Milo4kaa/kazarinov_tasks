test_string = '''
@VVV>>>>>>>>V<<VVVV<<<VV>>>
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

path = input()
char = path[0]
way_list = path[1:].split('V')
num_spaces = 0
for move in way_list:
    if move and move[0] == '<':
        num_spaces -= len(move)
    print(' '*num_spaces + char*(1+len(move)))
    if move and move[0] == '>':
        num_spaces += len(move)
test_string = '''
5
6122802
14406496
15230209
2541121
1758741
'''[1:-1].split('\n')[::-1]


def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp


a = int(input('Vvedite kolv blokov: '))
blockchain_right = True
for i in range(a):
    if i == 0:
        h1 = 0
    else:
        h1 = h
    b = int(input())
    h = b % 256
    b //= 256
    r = b % 256
    b //= 256
    m = b
    if ((h != 37 * (m + r + h1) % 256) or (h >= 100)) and blockchain_right:
        print(i)
        blockchain_right = False
if blockchain_right:
    print('-1')
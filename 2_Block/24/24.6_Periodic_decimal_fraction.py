test_string = '''
15
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

n = int(input())
r = 1
rr = []
dd = []
while r not in rr:
    rr.append(r)
    dd.append(10*r//n)
    r = 10*r%n
print(*dd[rr.index(r):])


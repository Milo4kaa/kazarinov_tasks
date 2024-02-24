test_string = '''
4
34
243
43
292
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

lst = []
n = int(input())
for i in range(n):
    num = int(input())
    lst.append(num)
for i in sorted(lst,reverse=True):
    print(i)

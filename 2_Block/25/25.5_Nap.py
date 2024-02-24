test_string = '''
3
стеклянный шарик
монета
жук
2
3
3
2
1
2
1
2

'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

n = int(input())
li = ['']*n
for i in range(n):
    li[i] = input()
k = int(input())
for i in range(k):
    x = int(input())
    tmp = ['']*x
    for j in range(x):
        tmp[j] = li[int(input())-1]
    li = tmp
for i in range(len(li)):
    print(li[i])
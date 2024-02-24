test_string = '''
4 3 1
Буря мглою небо кроет
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

nums = input().split(' ')
words = input().split(' ')
for i in nums:
    print(words[int(i)-1], end=" ")
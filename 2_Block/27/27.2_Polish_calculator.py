test_string = '''
10 15 - 7 *
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

s = input()

stack = []
for i in s.split(' '):
    try:
        stack.append(int(i))
    except ValueError:
        if i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        else:
            raise NotImplementedError

assert (len(stack) == 1)
print(stack[0])
test_string = '''
192
189
145
162
172
!
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
     if prompt:
        print(prompt)
     tmp = test_string.pop()
     print(tmp)
     return tmp

print('Введите рост участников:')
x = input()  
y = 0  
max = 0
min = 300
while x != '!':  
    x = int(x)  
    if 150 <= x <= 190:
        y += 1
        if x >= max:
            max = x
        if x <= min:
            min = x
    x = input()  
print('Количество подходящих:',y)  
print(min, max)
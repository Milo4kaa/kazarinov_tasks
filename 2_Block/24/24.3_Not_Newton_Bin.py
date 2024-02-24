test_string = '''
4
2
7
10
5
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

nums = list()
z = 0
number = int(input('Введите количество строк: '))
for i in range(number):
    num = int(input('Введите число: '))
    nums.append(num)
for i in range(number-1):
    print(nums[z]+nums[z+1])
    z += 1
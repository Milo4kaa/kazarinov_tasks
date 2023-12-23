nums = list()
z = 0
number = int(input('Введите количество строк: '))
for i in range(number):
    num = int(input('Введите число: '))
    nums.append(num)
for i in range(number-1):
    print(nums[z]+nums[z+1])
    z += 1
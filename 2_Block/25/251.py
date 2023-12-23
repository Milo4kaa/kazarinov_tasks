n = int(input('Введите количество чисел в наборе:'))
numbers = list()
for i in range(n):
    num = int(input('Введите число: '))
    numbers.append(num)
target = int(input('Введите конечное число: '))
z = False
for num in numbers:
    res = target / num
    if res in numbers and num != res:
        z = True
if z:
    print("ДА")
else:
    print("НЕТ")
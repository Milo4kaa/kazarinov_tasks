test_string = '''
фартинги
984
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

units = input("Введите единицы (фартинги или пенсы): ").lower()
sum = int(input("Введите сумму в указанных единицах: "))

if units == 'пенсы':
    sum *= 4

funts = sum // (20 * 12 * 4)
remainder = sum % (20 * 12 * 4)
shiling = remainder // (12 * 4)
remainder %= (12 * 4)
pens = remainder // 4
furting = remainder % 4

if funts > 0:
    print(f"Фунтов: {funts}")
if shiling > 0:
    print(f"Шиллингов: {shiling}")
if pens > 0:
    print(f"Пенсов: {pens}")
if furting > 0:
    print(f"Фартингов: {furting}")

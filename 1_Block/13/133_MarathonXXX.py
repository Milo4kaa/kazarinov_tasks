import math
test_string = '''
42
20
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

n = input("Введите длину маршрута: ")
m = input("Введите, сколько за день пробегает спортсмен: ")
z = int(n) / int(m)
z = math.ceil(z)
print(f"Спортсмену понадобится {z} дней для преодоление данной дистанции")

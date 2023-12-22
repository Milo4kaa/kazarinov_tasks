test_string = '''
110
130
120
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

a = int(input("Введите рост первого мальчика: "))
b = int(input("Введите рост второго мальчика: "))
c = int(input("Введите рост третьего мальчика: "))
mn = min(a, b, c)
mx = max(a, b, c)
sr = a + b + c - mx - mn
print(f"Ответ: {mx} {sr} {mn}")

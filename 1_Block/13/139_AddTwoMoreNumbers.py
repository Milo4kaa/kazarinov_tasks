test_string = '''
1.25
2.3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

print((float(input("Введите первое число: ")) + float(input('Ввелите второе число: '))))

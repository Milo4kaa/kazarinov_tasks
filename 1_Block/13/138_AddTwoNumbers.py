test_string = '''
34234324
52354436
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

print((int(input("Введите первое число: ")) + int(input('Введите второе число:'))))

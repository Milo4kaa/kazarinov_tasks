test_string = '''
1
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

a = int(input("Введите исходное число: "))
z = a
for i in range(4):
    z += 2
    a = (a + (z-1)) * z
print(a)
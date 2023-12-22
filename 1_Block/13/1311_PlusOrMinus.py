test_string = '''
3.14
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

z = float(input("Введите число: "))
if z > 0:
    print("+")
if z == 0:
    print("0")
if z < 0:
    print("-")

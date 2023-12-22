test_string = '''
38 попугаев и еще одно попугайское крылышко
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

print("Длина в попугаях\n")
a = input("Введите фразу: ")
print(len(a) // len("parrot"))

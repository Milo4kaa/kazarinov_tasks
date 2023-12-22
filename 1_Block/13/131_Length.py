test_string = '''
собака
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp
word = input("Введите слово: ")
a = len(word)
print(f"Слово {word} имеет длину {a}")

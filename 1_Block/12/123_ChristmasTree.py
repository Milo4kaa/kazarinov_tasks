test_string = '''
раз
два
три
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

print('Зажги ёлочка')
greek_letter_1 = input()
greek_letter_2 = input()
greek_letter_3 = input()
if greek_letter_1 == "раз" and greek_letter_2 == "два" and greek_letter_3 == "три":
    print("Гори!")
else:print("Не гори!")

test_string = '''
1
2
3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

print('Ёлочка Гори!')
greek_letter_1 = input()
greek_letter_2 = input()
greek_letter_3 = input()
if greek_letter_1 == 'раз' and greek_letter_2 == 'два' and greek_letter_3 == 'три' or greek_letter_1 == '1' and greek_letter_2 == '2' and greek_letter_3 == '3':
    print('ГОРИ.')
else:
    print('НЕ ГОРИ.')

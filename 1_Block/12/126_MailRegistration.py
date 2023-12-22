test_string = '''
Ml4k
ml4k@gmail.com
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp

greek_letter_1 = input("Логин")
greek_letter_2 = input("Адрес")
if "@" in greek_letter_1:
    print("Некорректный логин")
else:

    if "@" in greek_letter_2:
        print("OK")
        print("Вы зареганы")
    else:
        print("Некорректный адрес")

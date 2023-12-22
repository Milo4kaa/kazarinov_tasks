test_string = '''
да
да
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp


print('Yes or Not')

FirstLine = input("Введите первый ответ")
SecondLine = input("Введите второй ответ")

if (FirstLine == 'да' and SecondLine =="да" or FirstLine == "нет" and SecondLine =="нет" or FirstLine == "да" and SecondLine =="нет" or FirstLine == "нет" and SecondLine =="да"):
    print('Верно')
else:
    print("не верно")

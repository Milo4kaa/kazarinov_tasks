test_string = '''
Нижний Новгород
Тула
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp
july = input("Введите название первого города: ")
august = input("Введите название второго города ")
if (july == "Тула" and august == "Пенза") or (july == "Пенза" and august == "Тула"):
    print("Нет")
else:
    print("Да")

test_string = '''
Привет! Как дела?
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(tmp)
	return tmp


message = input("Введите сообщение: ")

price = len(message) * 40

rubles = price // 100
kopecks = price % 100

print(f"{rubles} р. {kopecks} коп.")
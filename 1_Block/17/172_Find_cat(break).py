test_string = '''
4
Как устроен типичный фрукт:
кожура;
мякоть;
косточки.
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

greek_letter_1 = int(input("Введите к-во строк: "))

for i in range(greek_letter_1):
    text = input('Введите строку: ').lower()
    if 'кот' in text:
       print('Мяу')
       break
if not 'кот' in text:
    print('нет')
test_string = '''
новгород
дублин
новгород
дублин
тула
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

x = 0
frst = input('Введите город: ')
while x < 1:
    city = input('Введите город: ')
    if city[0] == frst[-1]:
        frst = city
    else:
        x += 1
print(city)

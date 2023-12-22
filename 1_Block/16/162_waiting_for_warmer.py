test_string = '''
15.9
16.3
16.8
19.1
20.5
20.1
21.8
22.4
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

temp = []
weeks = 0
while True:
    temperature = float(input('Vvedite temperaturu: '))
    temp.append(temperature)
    if temperature >= 22.0:
        break
weeks = len(temp) // 7
print(weeks)



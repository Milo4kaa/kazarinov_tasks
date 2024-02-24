test_string = '''
3
SVO TRS 29481292
%%LJPZ DME 11113283675
####&%^^^^
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

number = int(input('Введите количество строк: '))
list = set()
for i in range(number):
    st = input('Введите строку: ')
    if st[:4] == '####':
        continue
    if '%' in st:
        st = st.replace('%', '')
    list.add(st)
for words in list:
    print(words)

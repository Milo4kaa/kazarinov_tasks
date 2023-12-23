number = int(input('Введите количество строк: '))
list = set()
for i in range(number):
    st = input('Введите строку: ')
    if '%' in st:
        st = st.replace('%', '')
        list.add(st)
    elif '####' not in st:
        list.add(st)
for words in list:
    print(words)

test_string = '''
ivanov:qwerty:100:1:Сергей Иванов, менеджер:/home/ivanov:/bin/sh
ilyina:gfhjkm:101:1:Мария Ильина, старший программист:HL3:/home/ilyina:/bin/sh
kuznetsova:jxtym[bnhsqgfhjkm:102:1:Дарья Кузнецова, младший программист:/home/kuznetsova:/bin/sh
polivanov:qwerty:103:1:Андрей Поливанов, младший программист:TF3:/home/polivanov:/bin/sh

123456;qwerty;password
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

passwd_content = []
tmp = input("Введите содержимое файла /etc/passwd: ")
while tmp:
    passwd_content.append(tmp)
    tmp = input()

common_passwords = input("Введите список самых часто используемых паролей: ").split(';')

for line in passwd_content:
    user_info = line.split(':')
    username = user_info[0]
    password = user_info[1]
    additional_info = user_info[4]

    if password in common_passwords:
        print("\nTo:", username)
        print(additional_info + ", ваш пароль слишком простой, смените его.")
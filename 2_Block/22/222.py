x = 0
frst = input('Введите город: ')
while x < 1:
    city = input('Введите город: ')
    if city[0] == frst[-1]:
        frst = city
    else:
        x += 1
print(city)

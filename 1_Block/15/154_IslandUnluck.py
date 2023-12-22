test_string = '''
12
9
2012

'''.strip().split('\n')[::-1]
def input(prompt=''):   
    if prompt:
        print(prompt) 
    tmp = test_string.pop()
    print(tmp)
    return tmp

def find_day_of_week(day, month, year):    
    if month < 3:
        month += 12
        year -= 1
    century = year // 100
    year = year % 100
    calc_day = day + ((13 * (month + 1)) // 5) + year + (year // 4) + (century // 4) - (2 * century) + 777    
    day_of_week = calc_day % 7
    return day_of_week

day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: ")) - 3
year = int(input("Введите год рождения: "))

day_of_week = find_day_of_week(day, month, year)
weekdays = {    
    1: "Понедельник",
    2: "Вторник",    
    3: "Среда",
    4: "Четверг",    
    5: "Пятница",
    6: "Суббота",    
    0: "Воскресенье"
}
print("День недели вашего рождения:", weekdays[day_of_week])
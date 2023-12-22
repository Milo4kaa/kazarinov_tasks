def check_power_of_two(number):
    if number <= 0:
        return "НЕТ"
    power = 0
    while number > 1:
        if number % 2 != 0:
            return "НЕТ"
        number = number // 2
        power += 1
    if number == 1:
        return f"Является 2 в степени {power}"
    else:
        return "НЕТ"

print("Введите число")
for testing_number in range(4, 26):
    result = check_power_of_two(testing_number)
    print(f"Для числа {testing_number}: {result}")


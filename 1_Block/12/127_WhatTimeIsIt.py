def determine_time_of_day(time):
    if time.isdigit():
        time = int(time)
        if time >= 5 and time <= 10:
            return "утро"
        elif time >= 11 and time <= 17:
            return "день"
        elif time >= 18 and time <= 22:
            return "вечер"
        elif time >= 23 or time <= 4:
            return "ночь"
        else:
            return "Ошибка"
    else:
        return "Ошибка"

for testing_string in range(4, 26):
    input_time = str(testing_string)
    time_of_day = determine_time_of_day(input_time)
    print(f"Время: {input_time} Сейчас: {time_of_day}")
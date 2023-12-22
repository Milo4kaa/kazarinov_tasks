import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Осталось секунд: {i}")
        time.sleep(1)
seconds = 5
countdown(seconds)
print("Пуск")
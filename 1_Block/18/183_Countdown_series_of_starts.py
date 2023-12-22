numb = int(input('Vvedite chislo zapuskov: '))
time = 0
for i in range(numb):
    time += 1
    for y in range(time,0 ,-1):
        print('Осталось секунд: ',y-1)
    print('Zapusk')

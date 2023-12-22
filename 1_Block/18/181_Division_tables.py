kol = int(input('Vvedite kolv kolonok: '))
stroka = int(input('Vvedite kolv strok: '))
for z in range(stroka):
    for i in range(kol):
        print(float(i+1)/(z+1), end=" ")
    print()

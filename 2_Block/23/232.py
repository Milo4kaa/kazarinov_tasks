number = int(input('Введите размер доски: '))
symb = 'ABCDEFGH'
for i in range(number, 0, -1):
    for j in symb[0:number]:
        print(j,i,sep="",end=" ")
    if j == symb[number-1]:
        print()


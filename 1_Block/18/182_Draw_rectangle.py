height = int(input('Vvedite visotu:'))
length = int(input('Vvedite dlinu: '))
symb = input('Vvedite symbol: ')
print(symb*length)
for i in range(1, length+1):
    print(symb,' '*(length-2),symb, sep="")
print(symb*length)

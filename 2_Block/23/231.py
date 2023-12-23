frst = input('Введите первое слово: ')
scnd = input('Введите второе слово: ')
b = 0
k = 0
for i in range(0, len(frst)):
    if frst[i] == scnd[i]:
        b+=1
for i in range(0, len(frst)):
    if frst[i] in scnd:
       k+=1
print(b,k-b)
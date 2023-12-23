n = int(input())
r = rr = []
dd = []
while r not in rr:
    rr.append(r)
    dd.append(10*r//n)
    r = 10*r%n
print(*dd[rr.index(r):])

test_string = '''
2
3
470
430
465
2
451
450
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
    if prompt:
        print(prompt)
    tmp = test_string.pop()
    print(tmp)
    return tmp

num_roads = int(input("Введите количество дорог: "))

max_height = 0
road_number = 0

for i in range(num_roads):
    num_tunnels = int(input("Введите количество туннелей для дороги {}: ".format(i+1)))
    road_max_height = 0
    for j in range(num_tunnels):
        tunnel_height = int(input("Введите высоту туннеля {}: ".format(j+1)))
        if tunnel_height < road_max_height or road_max_height == 0:
            road_max_height = tunnel_height
    if road_max_height > max_height:
        max_height = road_max_height
        road_number = i+1

print("Номер дороги:", road_number)
print("Максимальная высота грузовика:", max_height)
test_string = '''
9
10 18
17 15
25 21
0 21
1 16
25 29
24 24
8 26
10 20
'''.strip().split('\n')[::-1]

def user_input(prompt=''):
    if prompt:
        print(prompt)
    return test_string.pop()


def max_treasure_points(N, points):
    max_points = [1] * N
    for i in range(1, N):
        for j in range(i):
            if abs(points[i][0] - points[j][0]) % 10 == 0 or abs(points[i][1] - points[j][1]) % 10 == 0:
                max_points[i] = max(max_points[i], max_points[j] + 1)
    return max(max_points)

N = int(user_input())
points = []
for _ in range(N):
    x, y = map(int, user_input().split())
    points.append((x, y))

print(max_treasure_points(N, points))
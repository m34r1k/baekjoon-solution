n = int(input())
dot_list = []
for i in range(n):
    coords = list(map(int, input().split()))
    dot_list.append(coords)
dot_list.sort(key=lambda x: [x[1], x[0]])

for point in dot_list:
    print(point[0], point[1])
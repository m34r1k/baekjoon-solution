n = int(input())
scores = []
for i in range(n):
    name_list = input().split()
    scores.append(name_list)
scores.sort(key=lambda x: [-int(x[1]), int(x[2]), -int(x[3]), x[0]])
    
for score in scores:
    print(score[0])
n = int(input())
scores = []
for i in range(n):
    name_list = []
    scores = list(input().split())
    scores.append(name_list)
    scores.sort(key=lambda x: [x[1], x[2], x[3], x[0]])
    
for score in scores:
    print(score[0])
n = int(input()) #몇번 반복?
scores = []
for i in range(n):
    name_list = input().split() #이름, 국, 영, 수 가 적힌 줄 리스트에 넣기
    scores.append(name_list)
scores.sort(key=lambda x: [-int(x[1]), int(x[2]), -int(x[3]), x[0]]) #문제 조건
    
for score in scores:
    print(score[0])
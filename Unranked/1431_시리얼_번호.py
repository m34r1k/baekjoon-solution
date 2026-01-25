def get_sum(serial):
    default = 0
    for i in serial: 
        if i.isdigit(): #만약 i가 숫자라면
            default += int(i) #원래 있던 값에 더하기
    return default
    
n = int(input())
serials = []

for i in range(n):
    serials.append(input()) #시리얼 코드 추가
    serials.sort(key=lambda x: (len(x), get_sum(x), x)) #조건
    
for i in serials:
    print(i)
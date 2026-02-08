n = int(input()) #step 1
cards = [] #step 1
for i in range(n): #step 1
    card = int(input()) #step 1
    found = False #step 5
    for j in cards: #step 2
        if j[0] == card: #step 3
            found = True #step 5
            j[1] += 1 #step 3
            
    # if 리스트를 돌아봤을 때 같은 숫자가 없다면: #step 4
    if found == False: #리스트를 돌아봤을 때 같은 숫자가 없다면 #step 6
        cards.append([card, 1]) #step 2

cards.sort(key=lambda x: (-x[1], x[0])) #step 7
print(cards[0][0]) # step 8
    
# step 1
# 총 숫자의 갯수 입력받기
# cards 빈리스트 만들기
# 반복해서 숫자 받기

# step 2
# cards 리스트를 돌면서 같은 숫자가 있는지 확인
# problem: cards에 아무것도 없기 때문에 for문이 돌아가지 않음
# solution: for 문과 따로 cards에 숫자를 집어넣는 코드를 적었음
    
# step 3
# cards에 숫자가 들어갔기 때문에 for문이 돌아감
# for문에서는 입력 받은 숫자가 리스트 안의 숫자와 겹치는게 있다면 그 숫자의 개수를 늘림

# step 4
# problem: append가 계속 실행되기 때문에 숫자를 입력할때마다 계속 cards에 추가됨
# solution: cards는 리스트를 돌아봤을 때 같은 숫자가 없다면 추가해야 함

# step 5
# problem: for문 안의 카드를 찾았다는 것을 밖에 알려줘야 함
# solution: found라는 변수를 만들어서 for문 밖과 소통할 수 있게 함

# step 6
# found를 통해서 '리스트를 돌아봤을 때 같은 숫자가 없다면'이라는 조건을 if문으로 구현함

#step 7
#lambda를 이용하여 sort를 한다.
#가장 개수가 많은 정수 -> 가장 작은 것

#step 8:
#print를 한다.
    
    
    
    #[[1, 1]]
    #[[1, 1], [2, 1]]
    #[[1, 2], [2, 1]]
    #[[1, 2], [2, 2]]
    #[[1, 3], [2, 2]]
# cards.sort(key=lambda x: (x[0], x[1]))
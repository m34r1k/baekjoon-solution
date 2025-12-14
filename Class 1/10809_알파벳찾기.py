# 입력 받기
word = input()

# 알파벳 위치 저장할 리스트 (-1로 초기화)
positions = ["-1"] * 26

# 단어에서 각 알파벳의 첫 등장 위치 찾기
for i in range(len(word)):
    index = ord(word[i]) - ord('a')  # 알파벳의 인덱스 계산
    if positions[index] == "-1":      # 처음 등장한 경우에만 기록
        positions[index] = str(i)
        
# 결과 출력
print(" ".join(positions))
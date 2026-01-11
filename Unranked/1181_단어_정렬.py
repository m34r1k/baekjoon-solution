n = int(input())
word_list = []

for i in range(n):
    word = input()
    word_list.append((len(word), word))

word_list = list(set(word_list))   # 중복 제거
word_list.sort(key=lambda x: (x[0], x[1]))  # 길이순, 길이가 같으면 사전순

for i in word_list:
    print(i[1])
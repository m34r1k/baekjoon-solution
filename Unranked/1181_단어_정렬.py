n = int(input())
word_list = []
for i in range(n):
    word = input()
    word_list.append((len(word), word)) #[(3, 'but'), (1, 'i'), (4, 'wont'), (8, 'hesitate'), (2, 'no'), (4, 'more'), (2, 'no'), (4, 'more'), (2, 'it'), (6, 'cannot'), (4, 'wait'), (2, 'im'), (5, 'yours')]
    
    #중복 제거하기
    word_list.sort(key=lambda x: x[0])
    unique_word_list = set(word_list)
for i in unique_word_list:
    print(i[1])
num = int(input())
for i in range(num):
    word = ""
    s = input()
    s = s.split()
    for j in s[1]:
        word += j * int(s[0])
    print(word)
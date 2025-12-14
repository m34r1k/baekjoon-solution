a = int(input())
correct = 0
pt = 0

for i in range(a):
    quiz = input()
    for j in quiz:
        if j == "O":
            correct += 1
            pt += correct
        else:
            correct = 0
    print(pt)
    correct = 0
    pt = 0
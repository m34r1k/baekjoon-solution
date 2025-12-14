a = int(input())
b = int(input())
c = int(input())

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

ans = a * b * c
str_ans = str(ans)
for i in range(len(str_ans)):
    #0
    if str_ans[i] == "0":
        zero += 1
        #1
    elif str_ans[i] == "1":
        one += 1
        #2
    elif str_ans[i] == "2":
        two += 1
        #3
    elif str_ans[i] == "3":
        three += 1
        #4
    elif str_ans[i] == "4":
        four += 1
        #5
    elif str_ans[i] == "5":
        five += 1
        #6
    elif str_ans[i] == "6":
        six += 1
        #7
    elif str_ans[i] == "7":
        seven += 1
        #8
    elif str_ans[i] == "8":
        eight += 1
        #9
    elif str_ans[i] == "9":
        nine += 1
print(zero)
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)
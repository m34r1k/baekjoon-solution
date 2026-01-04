n = int(input())
people_list = []
for i in range(n):
    people = input().split()
    people_list.append(people)
people_list.sort()
for people in people_list:
    print(people[0] + " " + people[1])
list = []
for i in range(10):
    x = int(input())
    list.append(x % 42)
        
data = set(list)

print(len(data))
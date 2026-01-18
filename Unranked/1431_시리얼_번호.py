def get_sum(serial):
    default = 0
    for i in serial:
        if i.isdigit():
            default += int(i)
    return default
    
n = int(input())
serials = []

for i in range(n):
    serials.append(input())
    serials.sort(key=lambda x: (len(x), get_sum(x), x))
    
for i in serials:
    print(i)
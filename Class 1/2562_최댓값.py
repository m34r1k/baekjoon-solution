large = -1

for i in range(9):
    a = int(input())
    if a > large:
        large = a
        large_index = i + 1
    
print(large)
print(large_index)
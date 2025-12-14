n = int(input())
for i in range(n):
    row = ""
    row += (n - i - 1) * " "
    row += (i + 1) * "*"
    print(row)
    

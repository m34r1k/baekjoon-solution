n = int(input())
def serial_code(num):
    codes = []
    for i in range(num):
        code = input()
        codes.append(code)
    
    codes = codes.sort(key=lambda x: len(x))
    
    print(codes)
serial_code(n)
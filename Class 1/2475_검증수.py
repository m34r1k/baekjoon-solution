def verify(a, b, c, d, e):
    return (a*a +b*b + c*c+d*d+e*e) % 10
v, w, x, y, z = map(int, input().split())
print(verify(v, w, x, y, z))
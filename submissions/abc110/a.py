a, b, c = map(int, input().split())

A = 10*a+b+c
B = 10*b+a+c
C = 10*c+a+b
print(max(A, B, C))

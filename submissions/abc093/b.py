a, b, k = map(int, input().split())

if 2*k >= b-a+1:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, a+k):
        print(i)
    for j in range(b-k+1, b+1):
        print(j)

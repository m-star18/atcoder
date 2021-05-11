def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)

n = int(input())
x = list(map(int, input().split()))
if n==1:
    print(x[0])
else:
    element = gcd(x[0], x[1])
    if n==2:print(element)
    else:
        for i in range(2,n):
            element=gcd(element,x[i])
        print(element)

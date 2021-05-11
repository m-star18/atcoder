def f(n):
    if n%2 ==0:
        return n/2
    else:
        return 3*n+1

s = int(input())
a = [0] * 1
a[0] = s
ans = 1

for i in a:
    b = f(i)
    ans += 1
    if b in a:
        break
    a.append(b)
print(ans)

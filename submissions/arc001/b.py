import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = 0
if a < b:
    c = b
    d = a
    e = b - a
elif a == b:
    print(ans)
    sys.exit()
else:
    c = a
    d = b
    e = a - b
d = round((c-d)*2, -1)//2
c = 0
if d > e:
    ans += d-e
else:
    ans += e-d
if d >= 5:
    for i in range(40):
        if d-c >= 10:
            c += 10
            ans += 1
        else:
            c += 5
            ans += 1
        if d-c == 0:
            break
print(ans)

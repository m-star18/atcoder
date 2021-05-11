import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            cnt = (500*i) + (100*j) + (50*k)
            if x == cnt:
                ans += 1
                break
print(ans)

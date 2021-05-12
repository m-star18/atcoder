import sys
input = sys.stdin.readline

n = int(input())
check = [10, 100, 1000, 10000, 100000]
ans = 0
if n in check:
    ans = 10
else:
    n = str(n)
    for i in range(len(n)):
        ans += int(n[i])
print(ans)

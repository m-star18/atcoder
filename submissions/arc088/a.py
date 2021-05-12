import sys
input = sys.stdin.readline

x, y = map(int, input().split())
ans = 1
memo = x
for i in range(y):
    memo *= 2
    if memo > y:
        print(ans)
        exit()
    ans += 1

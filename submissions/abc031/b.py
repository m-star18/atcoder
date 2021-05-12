import sys
input = sys.stdin.readline

l, h = map(int, input().split())
n = int(input())
for i in range(n):
    a = int(input())
    if l <= a:
        if h < a:
            ans = -1
        else:
            ans = 0
    else:
        ans = l - a
    print(ans)

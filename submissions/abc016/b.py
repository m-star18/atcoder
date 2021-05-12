import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
cnt = 0
ans = ['!', '+', '-', '?']

if a + b == c:
    cnt += 1

if a - b == c:
    cnt += 2

print(ans[cnt])

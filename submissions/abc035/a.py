import sys
input = sys.stdin.readline

w, h = map(int, input().split())

if w / h == 4 / 3:
    ans = '4:3'
else:
    ans = '16:9'

print(ans)

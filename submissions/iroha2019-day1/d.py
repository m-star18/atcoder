# sys.stdin.readline()
import sys
input = sys.stdin.readline

n, x, y = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
for i in range(n//2):
    x += a.pop(0)
    y += a.pop(0)
if x > y:
    ans = 'Takahashi'
elif x < y:
    ans = 'Aoki'
else:
    ans = 'Draw'
print(ans)

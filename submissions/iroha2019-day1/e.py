# sys.stdin.readline()
import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
d = list(map(int, input().split()))
d = [0]+d+[n+1]
d.sort()
ans = n-b
for i in range(b+1):
    ans -= (d[i+1]-d[i]-1)//a
print(ans)

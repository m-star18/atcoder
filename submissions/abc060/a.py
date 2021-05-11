# sys.stdin.readline()
import sys
input = sys.stdin.readline

N, T = map(int, input().split())
t = list(map(int, input().split()))
vd = 0
ans = 0
for i in range(N-1):
    if t[i+1]-t[i] < T:
        vd += t[i+1]-t[i]
    else:
        ans += vd+T
        vd = 0
print(ans+T+vd)

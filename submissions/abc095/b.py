import sys
input = sys.stdin.readline

n, x = map(int, input().split())
m = [0]*n
cnt = 0
for i in range(n):
    m[i] = int(input())
    cnt += m[i]
ans = (x-cnt)//min(m)+n
print(ans)

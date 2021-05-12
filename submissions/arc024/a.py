import sys
input = sys.stdin.readline

L, R= map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
ans = 0

for i in l:
  if i in r:
    r.remove(i)
    ans += 1
      
print(ans)

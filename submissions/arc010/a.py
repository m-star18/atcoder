import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())
ans = 0

for i in range(m):
  c = int(input())
  ans += 1
  
  if n <= a:
    n += b
  
  n -= c
    
  if n < 0:
    print(ans)
    exit()
    
ans = 'complete'
print(ans)

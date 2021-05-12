import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

for i in range(n):
  n -= a
  if n <= 0:
    ans = 'Ant'
    break
  n -= b
  if n <= 0:
    ans = 'Bug'
    break
    
print(ans)

import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

if (b - a) % 2 == 0:
  ans = (b - a) // 2
  
elif (b - 1) < (n - a):
  ans = a + (b - a - 1) // 2
  
else:
  ans = n - b + 1 + abs(a - b + 1) // 2

print(ans)

import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

if a > b:
  ans = min(a - b, abs(b + 10 - a))

else:
  ans = min(b - a, abs(a + 10 - b))

print(ans)

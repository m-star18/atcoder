import sys
input = sys.stdin.readline

n, v_a, v_b, l = map(int, input().split())

for i in range(n):
  t = l / v_a
  l = t * v_b

print(round(l, 6))

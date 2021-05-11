import sys
input = sys.stdin.readline

n = int(input())
s = [''] * n
p = [''] * n
cnt = 0
ans = 'atcoder'

for i in range(n):
  s[i], p[i] = input().split()
  p[i] = int(p[i])
  cnt += p[i]

for i in range(n):
  if p[i] > cnt / 2:
    ans = s[i]
    break

print(ans)

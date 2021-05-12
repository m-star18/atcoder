import sys
input = sys.stdin.readline

c = int(input())
nml = [sorted(list(map(int, input().split()))) for i in range(c)]
ans = 1
for i in range(3):
  memo = 0
  for j in range(c):
    if nml[j][i] > memo:
      memo = nml[j][i]
  ans *= memo
print(ans)

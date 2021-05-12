import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(1, 10 ** 9):
  if len(set(str(i))) == 1:
    cnt += 1
    if cnt == n:
      ans = i
      break
      
print(ans)

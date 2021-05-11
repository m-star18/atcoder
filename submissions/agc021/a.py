import sys
input = sys.stdin.readline

n = int(input())
n = str(n)
ans = (len(n) - 1) * 9 + int(n[0])

for i in range(1, len(n)):
  if int(n[i]) != 9:
    ans -= 1
    break
    
print(ans)

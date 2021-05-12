import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
  a[i], b[i] = map(int, input().split())
  
index_b = a.index(max(a))
ans = max(a) + b[index_b]
print(ans)

n, m, b = map(int, input().split())
print(n)
for i in range(n):
  if i*2 <= n:
    print(i, i, 'U')
  else:
    print(i, i, 'D')

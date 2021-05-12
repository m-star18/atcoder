import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k = map(int, readline().split())
r, s, p = map(int, readline().split())
t = input()
ans = [0, 0, 0]
check = t[:k]
for i in range(k, n):
    if t[i] == check[i - k]:
        check += '?'
    else:
        check += t[i]
for i in range(n):
    if check[i] != check[i - k] or i < k:
        if check[i] == 'r':
            ans[0] += 1
        elif check[i] == 's':
            ans[1] += 1
        elif check[i] == 'p':
            ans[2] += 1
print(ans[0] * p + ans[1] * r + ans[2] * s)

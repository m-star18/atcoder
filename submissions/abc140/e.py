import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *p = map(int, read().split())
ans = 0
l = list(range(n))
r = list(range(n))
memo = [-1] * (n + 1)
for i, pp in enumerate(p):
    memo[pp] = i
for i, idx in enumerate(memo[1:], 1):
    l1 = idx - 1
    r1 = idx + 1
    while l1 >= 0 and l1 != l[l1]:
        l1 = l[l1]
    while r1 < n and r1 != r[r1]:
        r1 = r[r1]
    l[idx] = l1
    r[idx] = r1
    if l1 != -1:
        l2 = l1 - 1
        while l2 >= 0 and l2 != l[l2]:
            l2 = l[l2]
        ans += (l1 - l2) * (r1 - idx) * i
    if r1 != n:
        r2 = r1 + 1
        while r2 < n and r2 != r[r2]:
            r2 = r[r2]
        ans += (r2 - r1) * (idx - l1) * i
print(ans)

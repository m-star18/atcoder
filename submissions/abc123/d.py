import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x, y, z, k = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = list(map(int, read().split()))
ab = [0] * x * y
for i, aa in enumerate(a):
    for j, bb in enumerate(b):
        ab[i * y + j] = aa + bb
ab = sorted(ab, reverse=True)[:k]
c = sorted(c, reverse=True)
ans = [0] * k * z
for i, abab in enumerate(ab):
    for j, cc in enumerate(c):
        ans[i * z + j] = abab + cc
ans.sort(reverse=True)
print('\n'.join(map(str, ans[:k])))

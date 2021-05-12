import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
ans = [0] * n
for i, aa in enumerate(a):
    cnt = 1
    memo = aa
    while i + 1 != memo:
        cnt += 1
        memo = a[memo - 1]
    ans[i] = cnt
print(*ans)

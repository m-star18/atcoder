import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
p = [int(readline()) for _ in range(n)]
memo = [0] * n
for i, pp in enumerate(p):
    memo[pp - 1] = i
cnt = 1
ans = 0
for bf, af in zip(memo, memo[1:]):
    if bf < af:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 1
if ans < cnt:
    ans = cnt
print(n - ans)

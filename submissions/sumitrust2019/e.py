import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
ans = 1
mod = 10 ** 9 + 7
memo = [0, 0, 0]
for check in a:
    if check in memo:
        ans *= memo.count(check)
        ans %= mod
        memo[memo.index(check)] += 1
    else:
        print(0)
        exit()
print(ans)

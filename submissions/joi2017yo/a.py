import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

memo = [int(readline()) for _ in range(5)]
ans = 0
if memo[0] < 0:
    ans += abs(memo[0]) * memo[2]
    memo[0] = 0
if memo[0] == 0:
    ans += memo[3]
ans += (memo[1] - memo[0]) * memo[-1]
print(ans)

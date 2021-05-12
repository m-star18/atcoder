import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
memo = [[0] * n for _ in range(3)]
for i in range(n):
    memo[0][i], memo[1][i], memo[2][i] = map(int, readline().split())
for i in range(n):
    ans = 0
    for check in memo:
        if check.count(check[i]) == 1:
            ans += check[i]
    print(ans)

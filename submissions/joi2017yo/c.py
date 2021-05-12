import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m, d = map(int, readline().split())
s = [readline().rstrip().decode() for _ in range(n)]
cnt = 0
if m >= d:
    for i in range(n):
        memo = 0
        for j in range(m):
            if s[i][j] == '.':
                memo += 1
            else:
                memo = 0
            if memo >= d:
                cnt += 1
if n >= d:
    for i in range(m):
        memo = 0
        for j in range(n):
            if s[j][i] == '.':
                memo += 1
            else:
                memo = 0
            if memo >= d:
                cnt += 1
print(cnt)

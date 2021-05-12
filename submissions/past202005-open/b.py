import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m, q = map(int, readline().split())
memo = [n] * m
ans = [[] for _ in range(n)]
for _ in range(q):
    s = readline().rstrip().decode()
    if s[0] == '1':
        _, nn = s.split()
        v = 0
        for mm in ans[int(nn) - 1]:
            v += memo[mm]
        print(v)
    else:
        _, nn, mm = s.split()
        mm = int(mm) - 1
        memo[mm] = max(0, memo[mm] - 1)
        ans[int(nn) - 1].append(mm)

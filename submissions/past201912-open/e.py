import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, q = map(int, readline().split())
f = [['N'] * n for _ in range(n)]
for i in range(q):
    s = list(map(int, readline().split()))
    s[1] -= 1
    if s[0] == 1:
        s[2] -= 1
        f[s[1]][s[2]] = 'Y'
    if s[0] == 2:
        for i in range(n):
            if i == s[1]:
                continue
            if f[i][s[1]] == 'Y':
                f[s[1]][i] = 'Y'
    if s[0] == 3:
        b = []
        for i in range(n):
            if s[1] == i:
                continue
            if f[s[1]][i] == 'Y':
                b.append(i)
        a = set()
        for check in b:
            for i in range(n):
                if check == i or i == s[1]:
                    continue
                if f[check][i] == 'Y':
                    a.add(i)
        for i in range(n):
            if s[1] == i:
                continue
            if i in a:
                f[s[1]][i] = 'Y'
for ans in f:
    print(*ans, sep='')

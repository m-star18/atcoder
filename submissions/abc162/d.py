import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = readline().rstrip().decode()
ans = s.count('R') * s.count('G') * s.count('B')
for i, si in enumerate(s):
    for j, sj in enumerate(s[i + 1:]):
        k = 2 * (j + 1) + i
        if k >= n:
            break
        if si != sj and si != s[k] and sj != s[k]:
            ans -= 1
print(ans)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s = list(read().rstrip().decode())
ans = 0
for i in range(n):
    ans = max(ans, len(set(s[:i]) & set(s[i:])))
print(ans)

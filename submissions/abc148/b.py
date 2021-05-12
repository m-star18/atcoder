import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
s, t = input().split()
ans = ''
for i in range(n):
    ans += s[i] + t[i]
print(ans)

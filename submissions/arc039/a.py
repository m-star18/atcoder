import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b = map(int, readline().split())
ans = -999
if a >= 900:
    ans = int(str(a)[2]) + 990 - b
if a >= 990:
    ans = max(ans, 999 - b)
if b <= 199:
    ans = max(ans, a - (int(str(b)[2]) + 100))
if b <= 109:
    ans = max(ans, a - 100)
ans = max(a % 100 + 900 - b, a - (b % 100 + 100), ans)
print(ans)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ans = n // 11 * 2
if 1 <= n % 11 <= 6:
    ans += 1
elif 7 <= n % 11 <= 10:
    ans += 2
print(ans)

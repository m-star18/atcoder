import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = [int(readline()) for i in range(n)][::-1]
ans = 0
for i in range(n - 1):
    ans += a[i] // 2
    if a[i] % 2 == 1 and a[i + 1] != 0:
        a[i + 1] -= 1
        ans += 1
ans += a[-1] // 2
print(ans)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
c = list(map(int, readline().split()))
q = int(readline())
k = min(c[::2])
g = min(c)
pk = 0
pg = 0
ans = 0
for _ in range(q):
    s = list(map(int, readline().split()))
    if s[0] == 1 and c[s[1] - 1] - (pk if s[1] % 2 == 1 else 0) - pg >= s[2]:
        ans += s[2]
        c[s[1] - 1] -= s[2]
        if s[1] % 2 == 1:
            k = min(k, c[s[1] - 1])
        g = min(g, c[s[1] - 1])
    elif s[0] == 2 and k >= s[1]:
        ans += (n + 1) // 2 * s[1]
        k -= s[1]
        g = min(g, k)
        pk += s[1]
    elif s[0] == 3 and g >= s[1]:
        ans += s[1] * n
        g -= s[1]
        k -= s[1]
        pg += s[1]
print(ans)

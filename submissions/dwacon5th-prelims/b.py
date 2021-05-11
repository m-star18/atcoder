import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, *a = map(int, read().split())
now = []
ans = 0
for i, aa in enumerate(a):
    v = aa
    now.append(v)
    for aaa in a[i + 1:]:
        v += aaa
        now.append(v)
for m in range(40, -1, -1):
    ans *= 2
    cnt = 0
    bit = 1 << m
    nxt = []
    for num in now:
        if num & bit:
            cnt += 1
            nxt.append(num)
    if k <= cnt:
        ans += 1
        now = nxt
print(ans)

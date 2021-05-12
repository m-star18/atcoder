import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

t1, t2, a1, a2, b1, b2 = map(int, read().split())
v1 = t1 * (a1 - b1)
v2 = t2 * (a2 - b2)
if v1 > 0:
    v1 *= -1
    v2 *= -1
if v1 + v2 == 0:
    print('infinity')
elif v1 + v2 < 0:
    print(0)
else:
    s, t = divmod(-v1, v1 + v2)
    ans = s * 2
    if t != 0:
        ans += 1
    print(ans)

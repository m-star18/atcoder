import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *r = map(int, read().split())
if n < 3:
    print(0)
    exit()
ans = 1
high = None
for x, y in zip(r, r[1:]):
    if x < y:
        if not high or high is None:
            ans += 1
            high = True
    elif x > y:
        if high or high is None:
            ans += 1
            high = False
print(ans if ans > 2 else 0)

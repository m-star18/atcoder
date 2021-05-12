import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *d = map(int, read().split())
d.sort()
p = [0, 24]
m = [0, 24]
for i, dd in enumerate(d):
    if i % 2 == 0:
        p.append(dd)
        m.append(24 - dd)
    else:
        p.append(24 - dd)
        m.append(dd)
pp, mm = float('inf'), float('inf')
p.sort()
m.sort()
for (bp, ap, bm, am) in zip(p, p[1:], m, m[1:]):
    pp = min(pp, ap - bp)
    mm = min(mm, am - bm)
print(max(pp, mm))

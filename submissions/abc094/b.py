import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
a.sort()
tmp = float('inf')
index = 0
for i, aa in enumerate(a):
    v = abs(a[-1] / 2 - aa)
    if v < tmp:
        tmp = v
        index = i
print(a[-1], a[index])

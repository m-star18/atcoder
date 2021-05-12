import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
ans = []
for i in range(n):
    t = []
    aa = []
    for j in range(n):
        if i == j:
            continue
        h = a[min(i, j):max(i, j) + 1]
        t += [sum(h[::2])]
        aa += [sum(h[1::2])]
    ans += [t[aa.index(max(aa))]]
print(max(ans))

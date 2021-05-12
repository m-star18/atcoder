import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
aa = []
bb = []
for _ in range(n):
    a, b = map(int, readline().split())
    aa.append(a)
    bb.append(b)
aa.sort()
bb.sort()
if n % 2 == 1:
    print(bb[n // 2] - aa[n // 2] + 1)
else:
    print(bb[n // 2] + bb[n // 2 - 1] - aa[n // 2] - aa[n // 2 - 1] + 1)

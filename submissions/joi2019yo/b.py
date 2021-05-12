import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
x = list(map(int, readline().split()))
m, *a = map(int, read().split())
for aa in a:
    if aa == n or x[aa - 1] + 1 != x[aa]:
        x[aa - 1] += 1
        if x[aa - 1] >= 2019:
            x[aa - 1] = 2019
print('\n'.join(map(str, x)))

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
m = int(readline())
a = list(map(int, readline().split()))
b = [list(map(int, readline().split())) for _ in range(m)]
cnt = [0] * n
for aa, bb in zip(a, b):
    for i in range(n):
        if aa == bb[i]:
            cnt[i] += 1
        else:
            cnt[aa - 1] += 1
print('\n'.join(map(str, cnt)))

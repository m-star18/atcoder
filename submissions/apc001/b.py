import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, read().split()))
cnt = 0
for aa, bb in zip(a, b):
    v = bb - aa
    if bb > aa:
        v //= 2
    cnt += v
if cnt >= 0:
    print('Yes')
else:
    print('No')

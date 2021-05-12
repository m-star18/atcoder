import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a = list(map(int, readline().split()))
cnt = 0
memo = 0
for aa in a:
    if aa % 4 == 0:
        cnt += 1
    elif aa % 2 == 1:
        memo += 1
print('Yes' if (cnt >= memo - 1 and cnt + memo == n) or cnt >= memo else 'No')

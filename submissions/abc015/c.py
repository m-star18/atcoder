import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from itertools import product

n, k = map(int, readline().split())
t = [tuple(map(int, readline().split())) for _ in range(n)]
for check in product(*t):
    memo = 0
    for num in check:
        memo ^= num
    if memo == 0:
        print('Found')
        exit()
print('Nothing')

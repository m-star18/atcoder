import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from math import ceil

memo = [int(readline()) for _ in range(5)]
print(memo[0] - max(ceil(memo[1] / memo[3]), ceil(memo[2] / memo[4])))

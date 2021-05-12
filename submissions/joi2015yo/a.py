import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

memo = [int(readline()) for i in range(5)]
print(min(memo[0] * memo[-1], memo[1] + max(0, memo[-1] - memo[2]) * memo[3]))

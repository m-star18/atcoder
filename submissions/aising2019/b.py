import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
a, b = map(int, readline().split())
p = list(map(int, readline().split()))
memo = [0, 0, 0]
for check in p:
    if check <= a:
        memo[0] += 1
    elif a < check <= b:
        memo[1] += 1
    else:
        memo[2] += 1
print(min(memo))

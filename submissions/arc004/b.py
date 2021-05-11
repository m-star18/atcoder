import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *d = map(int, read().split())
print('{}\n{}'.format(sum(d), max(0, max(d) * 2 - sum(d))))

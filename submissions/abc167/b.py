import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c, k = map(int, read().split())
print(min(a, k) if a + b >= k else 2 * a + b - k)

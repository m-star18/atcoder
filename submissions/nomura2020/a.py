import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h1, m1, h2, m2, k = map(int, readline().split())
time = h2 * 60 + m2 - h1 * 60 - m1
ans = time - k
print(max(0, ans))

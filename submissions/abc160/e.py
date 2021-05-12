import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

x, y, a, b, c = map(int, readline().split())
p = sorted(list(map(int, readline().split())), reverse=True)
q = sorted(list(map(int, readline().split())), reverse=True)
r = list(map(int, readline().split()))
r += p[:x] + q[:y]
r.sort(reverse=True)
print(sum(r[:x + y]))

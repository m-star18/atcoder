import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
ta = [list(map(int, readline().split())) for _ in range(n)]
t, a = ta.pop(0)
for tt, aa in ta:
    v = max((t + tt - 1) // tt, (a + aa - 1) // aa)
    t = v * tt
    a = v * aa
print(t + a)

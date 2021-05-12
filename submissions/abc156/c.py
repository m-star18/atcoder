import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n = int(readline())
x = list(map(int, readline().split()))
v = [0] * 100
cnt = 0
for i in range(100):
    for xx in x:
        cnt += (xx - i) ** 2
    v[i] = cnt
    cnt = 0
print(min(v))

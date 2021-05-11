import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in range(m)]
ab.sort(key=lambda x: x[1])
cnt = 0
check = -1
for a, b in ab:
    if a <= check < b:
        continue
    check = b - 1
    cnt += 1
print(cnt)

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int, readline().split())
cnt = 0
for i in range(c):
    if i % 7 == 6:
        cnt += b
    cnt += a
    if cnt >= c:
        print(i + 1)
        exit()

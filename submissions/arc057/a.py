import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, k = map(int, readline().split())
if k == 0:
    print(2 * 10 ** 12 - a)
    exit()
for i in range(10000):
    if a >= 2 * 10 ** 12:
        print(i)
        exit()
    a += 1 + k * a

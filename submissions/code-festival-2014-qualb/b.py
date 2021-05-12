import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, *a = map(int, read().split())
cnt = 0
for d, aa in enumerate(a):
    cnt += aa
    if cnt >= k:
        print(d + 1)
        break

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, k, *t = map(int, read().split())
for i in range(n - 3):
    if k > sum(t[i:i + 3]):
        print(i + 3)
        break
else:
    print(-1)

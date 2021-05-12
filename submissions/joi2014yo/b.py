import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = [int(readline()) for _ in range(n)]
b = [int(readline()) for _ in range(m)]
cnt = [0] * n
for check in b:
    for i, aa in enumerate(a):
        if check >= aa:
            cnt[i] += 1
            break
print(cnt.index(max(cnt)) + 1)

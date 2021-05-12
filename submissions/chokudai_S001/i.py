import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
index = 0
v = 0
cnt = 0
for i in range(n):
    v += a[i]
    if v == n:
        cnt += 1
    elif v > n:
        for j in range(index, i):
            v -= a[index]
            index += 1
            if v <= n:
                if v == n:
                    cnt += 1
                break
print(cnt)

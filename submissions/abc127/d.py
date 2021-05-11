import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, m = map(int, readline().split())
a = list(map(int, readline().split()))
bc = [list(map(int, readline().split())) for _ in range(m)]
bc.sort(key=lambda x: -x[1])
a.sort()
idx = 0
for b, c in bc:
    while b > 0:
        if a[idx] < c:
            a[idx] = c
            idx += 1
            b -= 1
        else:
            break
        if idx >= n:
            print(sum(a))
            exit()
print(sum(a))

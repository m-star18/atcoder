import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

h, w = map(int, readline().split())
n = int(readline())
a = list(map(int, readline().split()))
idx = 0
for i in range(h):
    ans = []
    for j in range(w):
        if a[idx] == 0:
            idx += 1
        a[idx] -= 1
        ans.append(idx + 1)
    if i % 2 == 1:
        ans = ans[::-1]
    print(*ans)

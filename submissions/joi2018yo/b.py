import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
cnt = 1
ans = 1
for check in a:
    if check == 1:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
print(max(ans, cnt))
